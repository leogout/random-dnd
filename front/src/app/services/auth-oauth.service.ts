import { Injectable } from '@angular/core';
import { AuthConfig, OAuthService } from 'angular-oauth2-oidc';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthOAuthService {

  constructor(private oauthService: OAuthService) {
    this.configure();
  }

  private configure() {
    const googleAuthConfig: AuthConfig = {
      issuer: 'https://accounts.google.com',
      redirectUri: window.location.origin + '/index.html',
      clientId: environment.googleClientId,
      scope: 'openid profile email',
      strictDiscoveryDocumentValidation: false,
    };

    this.oauthService.configure(googleAuthConfig);
    this.oauthService.loadDiscoveryDocumentAndTryLogin();
  }

  login() {
    this.oauthService.initLoginFlow();
  }

  logout() {
    this.oauthService.logOut();
  }

  get isLoggedIn(): boolean {
    return this.oauthService.hasValidAccessToken();
  }

  get userName(): string {
    const claims = this.oauthService.getIdentityClaims();
    if (!claims) {
      return '';
    }
    return (claims as any).name;
  }
}
