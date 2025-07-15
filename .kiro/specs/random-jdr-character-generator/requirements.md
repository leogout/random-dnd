# Requirements Document

## Introduction

Random JDR is a web-based Dungeons & Dragons character generator that allows users to create random NPCs (Non-Player Characters) with AI-generated attributes. The application consists of an Angular frontend and a FastAPI backend that integrates with Mistral AI to generate creative character descriptions, quests, and loot. The system supports multiple races and languages, includes OAuth authentication, and is containerized for deployment with Kubernetes.

## Requirements

### Requirement 1

**User Story:** As a game master, I want to log in using Google OAuth2 before accessing any page of the frontend, so that my access to the character generator is secure and personalized.

#### Acceptance Criteria

1. WHEN a user accesses any page of the application without being authenticated THEN the system SHALL redirect them to the login page
2. WHEN a user clicks the login button THEN the system SHALL initiate Google OAuth2 authentication flow
3. WHEN a user successfully authenticates with Google THEN the system SHALL store their authentication token and redirect them to the main application
4. WHEN a user is authenticated THEN the system SHALL allow access to all application pages
5. WHEN a user logs out THEN the system SHALL clear their authentication token and redirect them to the login page

### Requirement 2

**User Story:** As a game master, I want to choose the language (French or English) in the navbar at the top of the screen, so that the application interface is displayed in my preferred language.

#### Acceptance Criteria

1. WHEN a user accesses the main application THEN the system SHALL display a language selector in the navbar
2. WHEN a user clicks the language selector THEN the system SHALL display French and English as available options
3. WHEN a user selects a language THEN the system SHALL update all interface text to the selected language
4. WHEN a user selects a language THEN the system SHALL persist this preference for future sessions
5. WHEN a user returns to the application THEN the system SHALL display the interface in their previously selected language
6. WHEN a user makes an API call THEN the system SHALL include the selected language in the request headers

### Requirement 3

**User Story:** As a game master, I want to choose a race and generate a character using the language selected in the navbar, so that I can quickly create NPCs with the appropriate localization for my campaigns.

#### Acceptance Criteria

1. WHEN a user accesses the character generation page THEN the system SHALL display a form with race selection options
2. WHEN a user views the race dropdown THEN the system SHALL display dwarf, elf, halfling, human, gnome, and half-orc as available options
3. WHEN a user selects a race and clicks generate THEN the system SHALL call the backend API with the selected race and current language preference
4. WHEN the API receives valid parameters THEN the system SHALL return a complete character with all required attributes localized in the selected language
5. WHEN the character is generated THEN the system SHALL display the character information on the page

### Requirement 4

**User Story:** As a game master, I want the generated characters to include comprehensive details, so that I can immediately use them in my campaigns without additional preparation.

#### Acceptance Criteria

1. WHEN a character is generated THEN the system SHALL include the character's race, full name, and gender
2. WHEN a character is generated THEN the system SHALL include a creative physical description
3. WHEN a character is generated THEN the system SHALL include the character's attitude toward players
4. WHEN a character is generated THEN the system SHALL include a list of loot items with names and descriptions
5. WHEN a character is generated THEN the system SHALL include a quest that the character can offer to players
6. WHEN the selected language is French THEN the system SHALL generate all text content in French
7. WHEN the selected language is English THEN the system SHALL generate all text content in English

### Requirement 5

**User Story:** As a system administrator, I want the application to be containerized and deployable, so that I can easily deploy and scale the application in different environments.

#### Acceptance Criteria

1. WHEN deploying the backend THEN the system SHALL run in a Docker container with all dependencies
2. WHEN deploying the frontend THEN the system SHALL run in a Docker container with nginx serving static files
3. WHEN deploying to Kubernetes THEN the system SHALL use Helm charts for configuration management
4. WHEN deploying THEN the system SHALL include PostgreSQL database with proper connection configuration
5. WHEN the application starts THEN the system SHALL provide health check endpoints for liveness and readiness probes

### Requirement 6

**User Story:** As a system administrator, I want the application to have proper monitoring and error handling, so that I can ensure system reliability and troubleshoot issues.

#### Acceptance Criteria

1. WHEN the backend starts THEN the system SHALL provide a database connectivity check endpoint
2. WHEN database connection fails THEN the system SHALL return appropriate error status and log the error
3. WHEN API requests are made THEN the system SHALL log relevant information for debugging
4. WHEN CORS requests are made from the frontend THEN the system SHALL allow requests from localhost:4200
5. WHEN the system encounters errors THEN the system SHALL handle them gracefully without crashing

### Requirement 7

**User Story:** As a developer, I want the application to have a clean architecture with separation of concerns, so that the codebase is maintainable and extensible.

#### Acceptance Criteria

1. WHEN examining the backend THEN the system SHALL separate configuration, models, and API logic into different modules
2. WHEN examining the frontend THEN the system SHALL use Angular components, services, and models with clear separation
3. WHEN making API calls THEN the system SHALL use a dedicated service layer
4. WHEN handling forms THEN the system SHALL use reactive forms with proper validation
5. WHEN displaying data THEN the system SHALL use reusable components with proper input/output binding