"""
Unit tests for authentication middleware.
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
from fastapi import HTTPException, Request
from fastapi.testclient import TestClient
import jwt
import json

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from auth import (
    extract_token_from_header,
    verify_google_oauth2_token,
    decode_jwt_token,
    validate_token,
    require_authentication,
    AuthenticationError
)


class TestExtractTokenFromHeader:
    """Test token extraction from Authorization header."""
    
    def test_extract_valid_bearer_token(self):
        """Test extracting valid Bearer token."""
        header = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        result = extract_token_from_header(header)
        assert result == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    
    def test_extract_token_none_header(self):
        """Test with None authorization header."""
        result = extract_token_from_header(None)
        assert result is None
    
    def test_extract_token_empty_header(self):
        """Test with empty authorization header."""
        result = extract_token_from_header("")
        assert result is None
    
    def test_extract_token_invalid_format(self):
        """Test with invalid authorization header format."""
        result = extract_token_from_header("InvalidFormat token123")
        assert result is None
    
    def test_extract_token_bearer_only(self):
        """Test with Bearer prefix only."""
        result = extract_token_from_header("Bearer ")
        assert result == ""


class TestVerifyGoogleOAuth2Token:
    """Test Google OAuth2 token verification."""
    
    @patch('auth.id_token.verify_oauth2_token')
    def test_verify_valid_google_token(self, mock_verify):
        """Test verification of valid Google OAuth2 token."""
        mock_user_info = {
            'iss': 'accounts.google.com',
            'email': 'test@example.com',
            'sub': '123456789',
            'name': 'Test User'
        }
        mock_verify.return_value = mock_user_info
        
        result = verify_google_oauth2_token("valid_token")
        
        assert result == mock_user_info
        mock_verify.assert_called_once()
    
    @patch('auth.id_token.verify_oauth2_token')
    def test_verify_invalid_issuer(self, mock_verify):
        """Test verification with invalid issuer."""
        mock_user_info = {
            'iss': 'invalid.issuer.com',
            'email': 'test@example.com'
        }
        mock_verify.return_value = mock_user_info
        
        with pytest.raises(AuthenticationError, match="Invalid token issuer"):
            verify_google_oauth2_token("invalid_token")
    
    @patch('auth.id_token.verify_oauth2_token')
    def test_verify_token_value_error(self, mock_verify):
        """Test verification with ValueError from Google library."""
        mock_verify.side_effect = ValueError("Invalid token format")
        
        with pytest.raises(AuthenticationError, match="Invalid token"):
            verify_google_oauth2_token("malformed_token")
    
    @patch('auth.id_token.verify_oauth2_token')
    def test_verify_token_unexpected_error(self, mock_verify):
        """Test verification with unexpected error."""
        mock_verify.side_effect = Exception("Unexpected error")
        
        with pytest.raises(AuthenticationError, match="Token verification error"):
            verify_google_oauth2_token("error_token")


class TestDecodeJWTToken:
    """Test JWT token decoding without verification."""
    
    def test_decode_valid_jwt(self):
        """Test decoding valid JWT token."""
        payload = {'sub': '123', 'email': 'test@example.com', 'exp': 1234567890}
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        result = decode_jwt_token(token)
        
        assert result['sub'] == '123'
        assert result['email'] == 'test@example.com'
    
    def test_decode_invalid_jwt(self):
        """Test decoding invalid JWT token."""
        with pytest.raises(AuthenticationError, match="Invalid JWT token"):
            decode_jwt_token("invalid.jwt.token")
    
    def test_decode_malformed_jwt(self):
        """Test decoding malformed JWT token."""
        with pytest.raises(AuthenticationError, match="Invalid JWT token"):
            decode_jwt_token("not_a_jwt_at_all")


class TestValidateToken:
    """Test token validation function."""
    
    @patch('auth.verify_google_oauth2_token')
    def test_validate_with_signature_verification(self, mock_verify):
        """Test token validation with signature verification."""
        mock_user_info = {'email': 'test@example.com'}
        mock_verify.return_value = mock_user_info
        
        result = validate_token("token", verify_signature=True)
        
        assert result == mock_user_info
        mock_verify.assert_called_once_with("token")
    
    @patch('auth.decode_jwt_token')
    def test_validate_without_signature_verification(self, mock_decode):
        """Test token validation without signature verification."""
        mock_payload = {'email': 'test@example.com'}
        mock_decode.return_value = mock_payload
        
        result = validate_token("token", verify_signature=False)
        
        assert result == mock_payload
        mock_decode.assert_called_once_with("token")


class TestRequireAuthentication:
    """Test authentication decorator."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.mock_request = Mock(spec=Request)
        self.mock_request.headers = {}
        self.mock_request.state = Mock()
    
    @patch('auth.validate_token')
    @pytest.mark.asyncio
    async def test_authentication_success(self, mock_validate):
        """Test successful authentication."""
        # Setup
        mock_user_info = {'email': 'test@example.com', 'sub': '123'}
        mock_validate.return_value = mock_user_info
        self.mock_request.headers = {"Authorization": "Bearer valid_token"}
        
        # Create decorated function
        @require_authentication()
        async def test_endpoint(request: Request):
            return {"message": "success", "user": request.state.user}
        
        # Execute
        result = await test_endpoint(self.mock_request)
        
        # Verify
        assert result["message"] == "success"
        assert self.mock_request.state.user == mock_user_info
        mock_validate.assert_called_once_with("valid_token", True)
    
    @pytest.mark.asyncio
    async def test_authentication_missing_header(self):
        """Test authentication with missing Authorization header."""
        @require_authentication()
        async def test_endpoint(request: Request):
            return {"message": "success"}
        
        with pytest.raises(HTTPException) as exc_info:
            await test_endpoint(self.mock_request)
        
        assert exc_info.value.status_code == 401
        assert "Missing or invalid authorization header" in exc_info.value.detail
    
    @pytest.mark.asyncio
    async def test_authentication_invalid_header_format(self):
        """Test authentication with invalid header format."""
        self.mock_request.headers = {"Authorization": "InvalidFormat token"}
        
        @require_authentication()
        async def test_endpoint(request: Request):
            return {"message": "success"}
        
        with pytest.raises(HTTPException) as exc_info:
            await test_endpoint(self.mock_request)
        
        assert exc_info.value.status_code == 401
        assert "Missing or invalid authorization header" in exc_info.value.detail
    
    @patch('auth.validate_token')
    @pytest.mark.asyncio
    async def test_authentication_token_validation_error(self, mock_validate):
        """Test authentication with token validation error."""
        mock_validate.side_effect = AuthenticationError("Invalid token")
        self.mock_request.headers = {"Authorization": "Bearer invalid_token"}
        
        @require_authentication()
        async def test_endpoint(request: Request):
            return {"message": "success"}
        
        with pytest.raises(HTTPException) as exc_info:
            await test_endpoint(self.mock_request)
        
        assert exc_info.value.status_code == 401
        assert "Invalid token" in exc_info.value.detail
    
    @patch('auth.validate_token')
    @pytest.mark.asyncio
    async def test_authentication_unexpected_error(self, mock_validate):
        """Test authentication with unexpected error."""
        mock_validate.side_effect = Exception("Unexpected error")
        self.mock_request.headers = {"Authorization": "Bearer token"}
        
        @require_authentication()
        async def test_endpoint(request: Request):
            return {"message": "success"}
        
        with pytest.raises(HTTPException) as exc_info:
            await test_endpoint(self.mock_request)
        
        assert exc_info.value.status_code == 500
        assert "Authentication service error" in exc_info.value.detail
    
    @patch('auth.validate_token')
    @pytest.mark.asyncio
    async def test_authentication_without_signature_verification(self, mock_validate):
        """Test authentication decorator without signature verification."""
        mock_user_info = {'email': 'test@example.com'}
        mock_validate.return_value = mock_user_info
        self.mock_request.headers = {"Authorization": "Bearer token"}
        
        @require_authentication(verify_signature=False)
        async def test_endpoint(request: Request):
            return {"user": request.state.user}
        
        result = await test_endpoint(self.mock_request)
        
        assert result["user"] == mock_user_info
        mock_validate.assert_called_once_with("token", False)


class TestIntegrationScenarios:
    """Integration tests for authentication scenarios."""
    
    @patch('auth.id_token.verify_oauth2_token')
    @pytest.mark.asyncio
    async def test_full_google_oauth_flow(self, mock_verify):
        """Test complete Google OAuth2 authentication flow."""
        # Setup Google token response
        mock_user_info = {
            'iss': 'accounts.google.com',
            'email': 'user@gmail.com',
            'sub': '123456789',
            'name': 'Test User',
            'picture': 'https://example.com/photo.jpg'
        }
        mock_verify.return_value = mock_user_info
        
        # Create request with Google OAuth2 token
        request = Mock(spec=Request)
        request.headers = {"Authorization": "Bearer google_oauth2_token"}
        request.state = Mock()
        
        # Create protected endpoint
        @require_authentication(verify_signature=True)
        async def protected_endpoint(request: Request):
            return {
                "message": "Access granted",
                "user_email": request.state.user['email'],
                "user_name": request.state.user['name']
            }
        
        # Execute
        result = await protected_endpoint(request)
        
        # Verify
        assert result["message"] == "Access granted"
        assert result["user_email"] == "user@gmail.com"
        assert result["user_name"] == "Test User"
        assert request.state.user == mock_user_info
    
    @pytest.mark.asyncio
    async def test_development_mode_authentication(self):
        """Test authentication in development mode (no signature verification)."""
        # Create JWT token for development
        payload = {
            'email': 'dev@example.com',
            'sub': '987654321',
            'name': 'Dev User'
        }
        dev_token = jwt.encode(payload, 'dev_secret', algorithm='HS256')
        
        # Create request
        request = Mock(spec=Request)
        request.headers = {"Authorization": f"Bearer {dev_token}"}
        request.state = Mock()
        
        # Create protected endpoint for development
        @require_authentication(verify_signature=False)
        async def dev_endpoint(request: Request):
            return {"user": request.state.user}
        
        # Execute
        result = await dev_endpoint(request)
        
        # Verify
        assert result["user"]["email"] == "dev@example.com"
        assert result["user"]["sub"] == "987654321"