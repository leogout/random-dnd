# Implementation Plan

## Backend Authentication Setup

- [ ] Install backend authentication dependencies
  - Install PyJWT library for token validation
  - Install google-auth library for Google OAuth2 token verification
  - Update requirements.txt or pyproject.toml with new dependencies
  - _Requirements: 1.1, 1.4_

- [ ] Create backend authentication middleware
  - Create auth.py module with token validation functions
  - Implement Google OAuth2 token verification function
  - Add JWT token decoding and validation logic
  - Create authentication decorator for protected endpoints
  - Write unit tests for authentication middleware functions
  - Test Google OAuth2 token verification with valid/invalid tokens
  - _Requirements: 1.1, 1.4_

- [ ] Add authentication to character generation endpoint
  - Apply authentication decorator to character generation endpoint
  - Extract user information from validated token
  - Add proper error responses for invalid/expired tokens (401, 403)
  - Write tests for authentication decorator functionality
  - Test error responses for authentication failures
  - Test authentication flow with valid and invalid tokens
  - _Requirements: 1.1, 1.4_

## Frontend Authentication Setup

- [ ] Install frontend OAuth2 dependencies
  - Install @google-cloud/oauth2 or google-auth-library-js
  - Install any additional JWT handling libraries if needed
  - Update package.json with new dependencies
  - _Requirements: 1.2, 1.3_

- [ ] Create AuthOAuthService
  - Create auth-oauth.service.ts with basic service structure
  - Implement login() method with Google OAuth2 integration
  - Implement logout() method to clear tokens and session
  - Add token storage methods (localStorage/sessionStorage)
  - Write unit tests for AuthOAuthService with mocked Google OAuth2
  - Test authentication state management and observables
  - Test token storage and retrieval methods
  - _Requirements: 1.2, 1.3_

- [ ] Add authentication state management to AuthOAuthService
  - Create authentication status observable (isAuthenticated$)
  - Implement token retrieval and validation methods
  - Add automatic token refresh logic if needed
  - Create user profile information methods
  - Test login/logout functionality
  - Test authentication state changes and observables
  - _Requirements: 1.2, 1.3_

- [ ] Create login component
  - Generate LoginComponent with Angular CLI
  - Add Google OAuth2 login button with proper styling
  - Implement click handler to trigger OAuth2 flow
  - Add basic error handling for login failures
  - Write unit tests for LoginComponent
  - Test OAuth2 redirect handling and token extraction
  - _Requirements: 1.2, 1.3_

- [ ] Implement OAuth2 redirect handling in login component
  - Add OAuth2 callback URL handling
  - Implement token extraction from OAuth2 response
  - Add success/error message display
  - Create navigation to main app after successful login
  - Test authentication flow integration
  - Test error handling for authentication failures
  - _Requirements: 1.2, 1.3_

- [ ] Create AuthGuard service
  - Generate AuthGuard service with Angular CLI
  - Implement canActivate method to check authentication status
  - Add redirect logic to login page for unauthenticated users
  - Create tests for AuthGuard route protection functionality
  - Test route protection functionality
  - _Requirements: 1.1, 1.4_

- [ ] Configure route protection
  - Apply AuthGuard to protected routes in app.routes.ts
  - Configure login route to be accessible without authentication
  - Add automatic redirect to main app after successful authentication
  - Test routing behavior for authenticated and unauthenticated users
  - Test complete authentication flow integration
  - _Requirements: 1.1, 1.4_

## Frontend Language and Navigation Setup

- [ ] Install internationalization dependencies
  - Install @angular/localize for Angular i18n support
  - Install Angular Material components for UI elements
  - Update package.json with new dependencies
  - _Requirements: 2.2, 2.3_

- [ ] Create LanguageService
  - Generate LanguageService with Angular CLI
  - Implement language preference storage methods (localStorage)
  - Create language switching functionality
  - Add language state observable for components to subscribe to
  - Write unit tests for LanguageService functionality
  - Test language preference storage and retrieval
  - Test language switching and state management
  - _Requirements: 2.2, 2.3, 2.4_

- [ ] Configure Angular i18n setup
  - Configure angular.json for internationalization
  - Create translation files for French (fr.json) and English (en.json)
  - Add basic interface text translations (login, logout, generate, etc.)
  - Set up language switching infrastructure
  - Test language persistence across application restarts
  - _Requirements: 2.2, 2.3, 2.4_

- [ ] Create navbar component structure
  - Generate NavbarComponent with Angular CLI
  - Add Angular Material toolbar and basic layout
  - Create component template with placeholder elements
  - Add basic styling and responsive design
  - Write unit tests for NavbarComponent
  - _Requirements: 2.1, 2.2_

- [ ] Add language selector to navbar
  - Implement language dropdown using Angular Material select
  - Add French and English language options
  - Connect dropdown to LanguageService for language switching
  - Add current language display and selection persistence
  - Test language selector dropdown functionality
  - _Requirements: 2.1, 2.2_

- [ ] Add authentication elements to navbar
  - Display user authentication status (logged in/out)
  - Add logout button that calls AuthOAuthService.logout()
  - Show user profile information when authenticated
  - Add conditional rendering based on authentication state
  - Test authentication status display
  - Test integration with LanguageService and AuthOAuthService
  - _Requirements: 2.1, 2.2_

- [ ] Integrate navbar into main application
  - Add NavbarComponent to main app component template
  - Configure navbar to appear on all authenticated pages
  - Test language switching across different components
  - Verify authentication status updates in real-time
  - Test integration across the entire application
  - _Requirements: 2.1, 2.2, 2.4, 2.5_

## Backend Character Generation Setup

- [ ] Update backend character generation endpoint for language support
  - Modify character generation endpoint to accept language parameter
  - Add validation for language parameter (fr/en)
  - Update endpoint to return proper error responses for invalid parameters
  - Write unit tests for character generation endpoint with language support
  - Test endpoint with different language parameters
  - Test error handling for invalid race/language parameters
  - _Requirements: 3.3, 3.4, 3.5_

- [ ] Enhance Mistral AI prompt generation with language support
  - Update prompt generation to include language specification
  - Create language-specific prompt templates for French and English
  - Ensure generated character content matches selected language
  - Create tests for Mistral AI integration with different languages
  - Test character generation in both languages
  - _Requirements: 3.3, 3.4, 3.5_

- [ ] Implement comprehensive character data model in backend
  - Update Character model to include all required fields (race, name, gender, description, attitude, loot, quest)
  - Modify character generation logic to populate all character fields
  - Add proper validation for race parameter (dwarf, elf, halfling, human, gnome, half-orc)
  - Write unit tests for character data model validation and generation
  - Test complete character data generation
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7_

## Frontend Character Generation Setup

- [ ] Create character generator component structure
  - Generate CharacterGeneratorComponent with Angular CLI
  - Create basic component template and styling
  - Add component to routing configuration
  - Set up component imports and dependencies
  - Write unit tests for CharacterGeneratorComponent
  - _Requirements: 3.1, 3.2_

- [ ] Implement race selection form
  - Add reactive form with FormBuilder and FormControl
  - Create race dropdown with options (dwarf, elf, halfling, human, gnome, half-orc)
  - Implement form validation for required race selection
  - Add form submission handling
  - Test race selection form validation and submission
  - _Requirements: 3.1, 3.2_

- [ ] Add loading states and UI feedback
  - Implement loading spinner during character generation
  - Add progress indicators and loading messages
  - Create disabled state for form during generation
  - Add success/error message display
  - Create tests for loading states and error handling
  - _Requirements: 3.1, 3.2_

- [ ] Create or update ApiService for character generation
  - Create ApiService if it doesn't exist, or update existing one
  - Implement character generation API call method
  - Add authentication headers to API requests
  - Include current language preference in API calls
  - Write unit tests for ApiService character generation calls
  - Test authentication header inclusion
  - Test language parameter inclusion in API calls
  - _Requirements: 3.3, 3.4_

- [ ] Add error handling and retry logic to ApiService
  - Implement proper error handling for authentication failures (401, 403)
  - Add error handling for API communication failures
  - Create retry logic for failed requests
  - Add timeout handling for long-running requests
  - Create tests for error handling and retry logic
  - Test integration with ApiService
  - _Requirements: 3.3, 3.4_

- [ ] Create character display component
  - Generate CharacterComponent with Angular CLI (or update existing)
  - Create template to display all character fields (race, name, gender, description, attitude, loot, quest)
  - Implement responsive design for character cards
  - Add proper styling with Angular Material components
  - Write unit tests for CharacterComponent
  - Test character data display and localization
  - _Requirements: 3.5_

- [ ] Add localization support to character display
  - Integrate character display with LanguageService
  - Add proper handling for localized character information
  - Ensure UI labels are translated based on selected language
  - Test character display in both French and English
  - Test integration with language switching
  - _Requirements: 3.5_

- [ ] Add accessibility features to character components
  - Add proper ARIA labels to all interactive elements
  - Implement keyboard navigation support
  - Add screen reader support for character information
  - Test accessibility with screen reader tools
  - Create tests for responsive design and accessibility features
  - _Requirements: 3.5_

- [ ] Integrate character generator with main application
  - Connect CharacterGeneratorComponent to ApiService
  - Wire up form submission to character generation API
  - Display generated character using CharacterComponent
  - Test complete character generation flow
  - Write integration tests for complete character generation flow
  - Create tests for error scenarios and edge cases
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_

