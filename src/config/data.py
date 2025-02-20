commit_types = {
    "feat": ["add", "implement", "new", "introduce"],
    "fix": ["fix", "resolve", "patch", "address"],
    "docs": ["document", "update docs", "readme"],
    "refactor": ["refactor", "restructure", "simplify"],
    "test": ["test", "coverage", "spec"],
    "style": ["format", "style", "lint"],
    "perf": ["optimize", "performance", "speed"],
    "chore": ["chore", "maintain", "update", "remove"],
    "ci": ["ci", "pipeline", "workflow"],
    "build": ["build", "dependency", "version"],
}

example_commits = {
    "feat": "feat(auth): implement OAuth2 with role-based access\n\nImplemented OAuth2 protocol with role-based control to enhance security and scalability.",
    "fix": "fix(api): resolve data race in concurrent requests\n\nFixed a race condition by adding synchronization mechanisms to prevent concurrent data modifications.",
    "docs": "docs(api): update authentication documentation\n\nUpdated API documentation to detail the new authentication methods and error handling procedures.",
    "refactor": "refactor(core): simplify error handling logic\n\nRefactored error handling to remove redundancies and improve code maintainability.",
    "chore": "chore(deps): update dependency versions to latest\n\nUpgraded dependencies to address security vulnerabilities and improve performance.",
    "style": "style(components): format according to style guide\n\nReformatted code to comply with style guidelines for better readability and consistency.",
    "perf": "perf(queries): optimize database index for faster lookups\n\nEnhanced database indexing strategy to improve query performance on large datasets.",
    "test": "test(api): add integration tests for payment flow\n\nAdded integration tests to ensure reliable and consistent performance of the payment processing system."
}

commit_training_data = {
    "feat": [
        "feat(auth): implement JWT authentication flow\n\nImplemented JWT-based authentication with token expiration handling to secure user sessions.",
        "feat(ui): add dark mode toggle with system preference detection\n\nAdded dark mode toggle that automatically adjusts based on system settings for improved user experience.",
        "feat(api): implement rate limiting middleware\n\nIntroduced rate limiting to prevent API abuse and ensure system stability under high load.",
        "feat(forms): add client-side form validation\n\nImplemented real-time form validation to provide immediate feedback and improve data integrity.",
        "feat(search): implement elasticsearch integration\n\nIntegrated Elasticsearch to boost search performance and enhance result accuracy.",
        "feat(cache): add Redis caching layer for API responses\n\nAdded a Redis caching layer to reduce response times and improve overall scalability.",
        "feat(auth): implement social login providers\n\nEnabled social login functionality to simplify the authentication process for users.",
        "feat(security): add two-factor authentication support\n\nIntroduced two-factor authentication to enhance account security and reduce fraud risks.",
    ],
    "fix": [
        "fix(auth): resolve token refresh race condition\n\nFixed a race condition in the token refresh logic by implementing proper synchronization mechanisms.",
        "fix(api): handle concurrent request deadlocks\n\nResolved API deadlocks by optimizing resource locking and request handling procedures.",
        "fix(validation): correct email regex pattern\n\nUpdated the email validation regex to accurately handle various valid email formats.",
        "fix(memory): resolve memory leak in WebSocket connections\n\nAddressed a memory leak by ensuring WebSocket connections are properly closed after use.",
        "fix(security): patch SQL injection vulnerability\n\nPatched a SQL injection vulnerability by sanitizing user inputs and using parameterized queries.",
        "fix(cors): resolve cross-origin request issues\n\nAdjusted CORS settings to correctly handle cross-origin requests and improve security.",
        "fix(cache): handle cache invalidation edge cases\n\nFixed issues with cache invalidation to ensure data consistency across different layers.",
        "fix(ui): resolve mobile viewport rendering issues\n\nCorrected viewport meta tag settings to improve rendering on mobile devices.",
    ],
    "docs": [
        "docs(api): update REST endpoints documentation\n\nRevised REST API documentation to include detailed information on new endpoints and error handling.",
        "docs(setup): improve installation instructions\n\nEnhanced installation guide with step-by-step instructions and troubleshooting tips for new users.",
        "docs(auth): document OAuth2 implementation details\n\nProvided comprehensive documentation covering OAuth2 flows, configuration, and security considerations.",
        "docs(deploy): add AWS deployment guide\n\nCreated a detailed guide for deploying the application on AWS, including best practices and configuration tips.",
        "docs(contributing): update PR guidelines\n\nUpdated contributing guidelines to reflect new review processes and code standards.",
        "docs(api): add GraphQL schema documentation\n\nIncluded detailed documentation for the GraphQL schema to help developers understand query structures.",
        "docs(security): document security best practices\n\nOutlined security best practices and compliance requirements for developers and auditors.",
        "docs(testing): update e2e testing guide\n\nRevised the end-to-end testing documentation with new scenarios and tool integrations.",
    ],
    "refactor": [
        "refactor(api): split monolithic controller into modules\n\nRefactored the API controller into modular components to enhance maintainability and scalability.",
        "refactor(db): optimize database query patterns\n\nImproved database performance by optimizing complex queries and reducing unnecessary joins.",
        "refactor(auth): separate authentication logic\n\nIsolated authentication logic into a dedicated module for clearer structure and easier testing.",
        "refactor(middleware): improve error handling flow\n\nStreamlined error handling within middleware to ensure consistent responses across the application.",
        "refactor(utils): create shared utility functions\n\nExtracted common code into shared utilities to reduce duplication and simplify maintenance.",
        "refactor(services): implement repository pattern\n\nAdopted the repository pattern in the services layer to decouple business logic from data access.",
        "refactor(validation): centralize validation logic\n\nCentralized various validation routines into a single module for consistency and reuse.",
        "refactor(config): improve configuration management\n\nRefactored configuration handling by separating environment-specific settings into distinct files.",
    ],
    "chore": [
        "chore(deps): update package dependencies to latest\n\nUpgraded all package dependencies to their latest versions to address security issues and improve performance.",
        "chore(ci): update GitHub Actions workflow\n\nRevised the CI pipeline to streamline automated testing and deployment processes.",
        "chore(docker): optimize container build process\n\nOptimized the Dockerfile to reduce image build times and improve container efficiency.",
        "chore(lint): update ESLint configuration\n\nUpdated ESLint rules to enforce new coding standards and remove deprecated configurations.",
        "chore(git): update gitignore patterns\n\nRefined the .gitignore file to exclude unnecessary files and reduce repository clutter.",
        "chore(deps): remove unused dependencies\n\nCleaned up the project by removing outdated and unused dependencies to simplify maintenance.",
        "chore(scripts): update build scripts\n\nEnhanced build scripts for better readability and efficiency during the deployment process.",
        "chore(types): update TypeScript definitions\n\nUpdated TypeScript definition files to reflect recent changes in the codebase.",
    ],
    "style": [
        "style(css): align with design system guidelines\n\nUpdated CSS styles to conform with the latest design system standards for better consistency.",
        "style(components): update button styling\n\nRefined button styling to improve visual hierarchy and overall usability in the UI.",
        "style(layout): improve responsive grid system\n\nEnhanced the grid layout to ensure consistent behavior across multiple device sizes.",
        "style(theme): update color palette variables\n\nModified theme variables to reflect new branding and improve the overall aesthetic appeal.",
        "style(forms): standardize input field styling\n\nStandardized the styling of form inputs for a cohesive look throughout the application.",
        "style(fonts): update typography system\n\nUpdated typography settings to enhance readability and maintain visual consistency.",
        "style(animations): refine transition effects\n\nImproved transition effects for smoother animations and better user interaction.",
        "style(icons): update icon system to SVG\n\nReplaced icon fonts with SVG icons to ensure scalability and clarity on all devices.",
    ],
    "perf": [
        "perf(images): implement lazy loading strategy\n\nImplemented lazy loading for images to defer off-screen loading and improve page load times.",
        "perf(api): add query result caching\n\nIntroduced caching for API query results to reduce response times and lower server load.",
        "perf(db): optimize database indices\n\nRevised database indices to accelerate query performance and reduce data retrieval latency.",
        "perf(bundle): reduce JavaScript bundle size\n\nMinimized bundle size by removing unused code and optimizing dependency imports.",
        "perf(assets): implement CDN distribution\n\nConfigured CDN distribution for static assets to boost load times and global accessibility.",
        "perf(queries): optimize database join operations\n\nEnhanced join query efficiency to better handle large datasets and reduce processing time.",
        "perf(cache): implement LRU caching strategy\n\nAdopted an LRU caching strategy to improve memory management and response speed.",
        "perf(api): implement response compression\n\nEnabled compression for API responses to decrease payload size and improve transfer speeds.",
    ],
    "test": [
        "test(api): add integration tests for auth flow\n\nAdded comprehensive integration tests to validate the authentication flow under various scenarios.",
        "test(ui): add unit tests for form validation\n\nImplemented unit tests to ensure that all form validations perform correctly and reliably.",
        "test(e2e): add checkout flow tests\n\nDeveloped end-to-end tests to simulate the complete checkout process and identify any issues.",
        "test(utils): improve test coverage for helpers\n\nEnhanced test coverage for utility functions to catch edge cases and improve overall stability.",
        "test(auth): add OAuth callback tests\n\nAdded tests specifically for OAuth callback functionality to ensure proper third-party integration.",
        "test(api): add load testing scenarios\n\nImplemented load testing to evaluate API performance under high traffic conditions.",
        "test(security): add penetration testing suite\n\nIntroduced a penetration testing suite to identify and mitigate potential security vulnerabilities.",
        "test(performance): add benchmark tests\n\nAdded benchmark tests to measure performance improvements and track regression over time.",
    ],
}

semantic_patterns = {
    "feat": [
        # New functionality
        ("create", "new"),
        ("add", "feature"),
        ("implement", "new"),
        ("enable", "support"),
        ("introduce", "capability"),
        ("build", "new"),
        ("develop", "feature"),
        ("set up", "new"),
        ("setup", "new"),
        ("establish", "new"),
        ("deploy", "new"),
        # Integration patterns
        ("integrate", "with"),
        ("connect", "to"),
        ("link", "with"),
        ("support", "for"),
        ("enable", "integration"),
        ("add", "support"),
        # User-facing changes
        ("allow", "users"),
        ("provide", "ability"),
        ("enable", "users"),
        ("add", "option"),
        ("implement", "interface"),
        ("create", "endpoint"),
        # System capabilities
        ("extend", "functionality"),
        ("expand", "capabilities"),
        ("enhance", "system"),
        ("upgrade", "functionality"),
        ("initialize", "system"),
        ("bootstrap", "application"),
        # Specific tech additions
        ("implement", "api"),
        ("add", "route"),
        ("create", "middleware"),
        ("setup", "database"),
        ("configure", "service"),
        ("establish", "connection"),
        ("add", "validation"),
        ("implement", "authentication"),
    ],
    "fix": [
        # Error handling
        ("correct", "issue"),
        ("prevent", "error"),
        ("resolve", "bug"),
        ("handle", "case"),
        ("patch", "vulnerability"),
        ("address", "problem"),
        ("solve", "issue"),
        ("eliminate", "error"),
        ("fix", "crash"),
        ("repair", "broken"),
        ("mitigate", "risk"),
        ("catch", "error"),
        # Security fixes
        ("patch", "security"),
        ("fix", "vulnerability"),
        ("secure", "endpoint"),
        ("prevent", "breach"),
        ("protect", "against"),
        ("sanitize", "input"),
        # Edge cases
        ("handle", "edge"),
        ("address", "corner"),
        ("fix", "rare"),
        ("resolve", "special"),
        ("cover", "exceptional"),
        ("manage", "unexpected"),
        # System issues
        ("correct", "behavior"),
        ("fix", "performance"),
        ("resolve", "conflict"),
        ("repair", "connection"),
        ("restore", "functionality"),
        ("fix", "race condition"),
        # Data issues
        ("correct", "data"),
        ("fix", "corruption"),
        ("resolve", "inconsistency"),
        ("repair", "state"),
        ("fix", "synchronization"),
        ("handle", "invalid"),
    ],
    "docs": [
        # Documentation updates
        ("explain", "how"),
        ("clarify", "docs"),
        ("document", "usage"),
        ("update", "readme"),
        ("improve", "documentation"),
        ("describe", "process"),
        ("add", "examples"),
        ("detail", "setup"),
        ("expand", "guide"),
        # API documentation
        ("document", "api"),
        ("describe", "endpoint"),
        ("specify", "parameters"),
        ("explain", "response"),
        ("detail", "authentication"),
        ("clarify", "usage"),
        # Guides and tutorials
        ("add", "tutorial"),
        ("create", "guide"),
        ("write", "documentation"),
        ("provide", "example"),
        ("explain", "workflow"),
        ("document", "steps"),
        # Technical writing
        ("revise", "documentation"),
        ("rewrite", "explanation"),
        ("elaborate", "on"),
        ("clarify", "section"),
        ("update", "guide"),
        ("improve", "clarity"),
        ("enhance", "readability"),
    ],
    "refactor": [
        # Code improvement
        ("improve", "code"),
        ("clean", "up"),
        ("simplify", "logic"),
        ("restructure", "code"),
        ("optimize", "performance"),
        ("enhance", "readability"),
        ("reorganize", "files"),
        # Architecture changes
        ("modernize", "codebase"),
        ("consolidate", "logic"),
        ("streamline", "process"),
        ("decouple", "from"),
        ("extract", "into"),
        ("separate", "concerns"),
        # Code organization
        ("move", "logic"),
        ("split", "into"),
        ("combine", "into"),
        ("organize", "better"),
        ("structure", "properly"),
        # Performance optimization
        ("optimize", "for"),
        ("improve", "efficiency"),
        ("enhance", "performance"),
        ("better", "handling"),
        # Technical debt
        ("reduce", "complexity"),
        ("simplify", "implementation"),
        ("clean", "architecture"),
        ("improve", "structure"),
    ],
    "chore": [
        # Maintenance
        ("remove", "unused"),
        ("delete", "old"),
        ("update", "version"),
        ("clean", "up"),
        ("maintain", "deps"),
        ("bump", "version"),
        # Organization
        ("organize", "files"),
        ("move", "to"),
        ("rename", "files"),
        ("restructure", "folders"),
        ("relocate", "assets"),
        # Dependencies
        ("upgrade", "packages"),
        ("update", "dependencies"),
        ("install", "package"),
        ("migrate", "to"),
        # Configuration
        ("configure", "setting"),
        ("setup", "config"),
        ("update", "environment"),
        ("modify", "setting"),
        # Automation
        ("automate", "process"),
        ("script", "task"),
        ("update", "workflow"),
        ("improve", "pipeline"),
    ],
    "style": [
        # Code style
        ("format", "code"),
        ("align", "with"),
        ("style", "according"),
        ("standardize", "format"),
        ("indent", "properly"),
        ("apply", "prettier"),
        ("enforce", "style"),
        # Consistency
        ("consistent", "formatting"),
        ("follow", "convention"),
        ("maintain", "standard"),
        ("uniform", "style"),
        # Visual changes
        ("adjust", "spacing"),
        ("align", "elements"),
        ("improve", "layout"),
        ("fix", "indentation"),
        # Standards compliance
        ("comply", "with"),
        ("match", "standard"),
        ("follow", "guidelines"),
        ("adhere", "to"),
    ],
    "perf": [
        # Speed optimization
        ("optimize", "speed"),
        ("improve", "performance"),
        ("reduce", "time"),
        ("decrease", "memory"),
        ("enhance", "efficiency"),
        ("speed", "up"),
        # Resource usage
        ("minimize", "load"),
        ("reduce", "usage"),
        ("optimize", "memory"),
        ("improve", "utilization"),
        # Response time
        ("faster", "response"),
        ("reduce", "latency"),
        ("improve", "speed"),
        ("quicken", "process"),
        # System performance
        ("efficient", "handling"),
        ("optimize", "processing"),
        ("improve", "throughput"),
        ("enhance", "capacity"),
        # Caching
        ("cache", "results"),
        ("implement", "caching"),
        ("optimize", "cache"),
        ("improve", "caching"),
    ],
    "test": [
        # Test creation
        ("add", "tests"),
        ("create", "test"),
        ("implement", "testing"),
        ("write", "test"),
        ("develop", "tests"),
        # Coverage
        ("cover", "cases"),
        ("increase", "coverage"),
        ("improve", "coverage"),
        ("extend", "tests"),
        # Validation
        ("ensure", "works"),
        ("verify", "behavior"),
        ("validate", "input"),
        ("check", "output"),
        # Test types
        ("unit", "test"),
        ("integration", "test"),
        ("e2e", "test"),
        ("regression", "test"),
        # Test improvements
        ("enhance", "tests"),
        ("strengthen", "testing"),
        ("improve", "reliability"),
        ("robust", "testing"),
    ],
    "ci": [
        # Pipeline
        ("update", "pipeline"),
        ("modify", "workflow"),
        ("improve", "ci"),
        ("configure", "build"),
        # Automation
        ("automate", "deploy"),
        ("setup", "action"),
        ("configure", "webhook"),
        ("add", "trigger"),
        # Integration
        ("integrate", "with"),
        ("connect", "to"),
        ("setup", "integration"),
        ("enable", "sync"),
        # Deployment
        ("improve", "deploy"),
        ("optimize", "release"),
        ("automate", "publish"),
        ("streamline", "delivery"),
    ],
}
