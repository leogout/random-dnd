"""
Authentication middleware for Google OAuth2 JWT token validation.
"""
import jwt
from functools import wraps
from typing import Optional, Dict, Any, Callable
from fastapi import HTTPException, Request, status
from google.auth.transport import requests
from google.oauth2 import id_token
import logging

logger = logging.getLogger('uvicorn.error')


class AuthenticationError(Exception):
    """Custom exception for authentication errors."""
    pass


def extract_token_from_header(authorization_header: Optional[str]) -> Optional[str]:
    """
    Extract JWT token from Authorization header.
    
    Args:
        authorization_header: The Authorization header value
        
    Returns:
        The JWT token string or None if not found
    """
    if not authorization_header:
        return None
    
    if not authorization_header.startswith("Bearer "):
        return None
    
    return authorization_header[7:]  # Remove "Bearer " prefix


def verify_google_oauth2_token(token: str) -> Dict[str, Any]:
    """
    Verify Google OAuth2 JWT token and extract user information.
    
    Args:
        token: The JWT token to verify
        
    Returns:
        Dictionary containing user information from the token
        
    Raises:
        AuthenticationError: If token verification fails
    """
    try:
        # Verify the token with Google's public keys
        idinfo = id_token.verify_oauth2_token(
            token, 
            requests.Request(),
            # Accept tokens from any Google OAuth2 client
            audience=None
        )
        
        # Verify the issuer
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise AuthenticationError("Invalid token issuer")
        
        logger.info(f"Successfully verified token for user: {idinfo.get('email', 'unknown')}")
        return idinfo
        
    except ValueError as e:
        logger.error(f"Token verification failed: {str(e)}")
        raise AuthenticationError(f"Invalid token: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error during token verification: {str(e)}")
        raise AuthenticationError(f"Token verification error: {str(e)}")


def decode_jwt_token(token: str) -> Dict[str, Any]:
    """
    Decode JWT token without verification (for development/testing).
    
    Args:
        token: The JWT token to decode
        
    Returns:
        Dictionary containing token payload
        
    Raises:
        AuthenticationError: If token decoding fails
    """
    try:
        # Decode without verification (for development purposes)
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded
    except jwt.InvalidTokenError as e:
        logger.error(f"JWT decoding failed: {str(e)}")
        raise AuthenticationError(f"Invalid JWT token: {str(e)}")


def validate_token(token: str, verify_signature: bool = True) -> Dict[str, Any]:
    """
    Validate JWT token and return user information.
    
    Args:
        token: The JWT token to validate
        verify_signature: Whether to verify the token signature with Google
        
    Returns:
        Dictionary containing user information
        
    Raises:
        AuthenticationError: If token validation fails
    """
    if verify_signature:
        return verify_google_oauth2_token(token)
    else:
        return decode_jwt_token(token)


def require_authentication(verify_signature: bool = True):
    """
    Decorator to protect FastAPI endpoints with authentication.
    
    Args:
        verify_signature: Whether to verify token signature with Google
        
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            # Extract token from Authorization header
            authorization_header = request.headers.get("Authorization")
            token = extract_token_from_header(authorization_header)
            
            if not token:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Missing or invalid authorization header",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
            try:
                # Validate the token
                user_info = validate_token(token, verify_signature)
                
                # Add user info to request state for use in endpoint
                request.state.user = user_info
                
                # Call the original function
                return await func(request, *args, **kwargs)
                
            except AuthenticationError as e:
                logger.warning(f"Authentication failed: {str(e)}")
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=str(e),
                    headers={"WWW-Authenticate": "Bearer"},
                )
            except Exception as e:
                logger.error(f"Unexpected authentication error: {str(e)}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Authentication service error"
                )
        
        return wrapper
    return decorator


# Convenience decorators
authenticated = require_authentication(verify_signature=True)
authenticated_dev = require_authentication(verify_signature=False)