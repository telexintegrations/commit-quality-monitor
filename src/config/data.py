commit_types = {
    "feat": [
        "add", "implement", "introduce", "enable", "support", "create", "integrate",
        "launch", "expand", "extend", "enhance", "develop", "prototype", "establish", "apply"
    ],
    "fix": [
        "fix", "resolve", "patch", "address", "correct", "repair", "handle", "debug",
        "mitigate", "eliminate", "hotfix", "prevent", "recover", "rollback", "restore", "sanitize"
    ],
    "docs": [
        "document", "update", "revise", "clarify", "explain", "annotate", "expand",
        "rewrite", "summarize", "edit", "describe", "correct", "detail", "review", "comment"
    ],
    "refactor": [
        "refactor", "restructure", "simplify", "cleanup", "redesign", "revamp", "reorganize",
        "rework", "modularize", "decompose", "deduplicate", "optimize", "streamline", "improve"
    ],
    "test": [
        "test", "cover", "validate", "verify", "mock", "benchmark", "assert",
        "simulate", "automate", "debug", "execute", "configure tests", "extend tests", "fix tests"
    ],
    "style": [
        "format", "style", "lint", "reformat", "standardize", "align", "adjust",
        "fix formatting", "apply conventions", "refine", "clean up", "improve consistency", "update style"
    ],
    "perf": [
        "optimize", "improve", "accelerate", "reduce", "enhance", "boost", "scale",
        "compress", "minimize", "streamline", "increase efficiency", "refine performance", "cache"
    ],
    "chore": [
        "maintain", "update", "remove", "tidy", "clean up", "upgrade", "refine",
        "adjust", "improve", "synchronize", "configure", "manage", "enhance workflow", "fix config"
    ],
    "ci": [
        "configure", "update", "fix", "automate", "optimize", "improve", "adjust",
        "modify", "setup", "enhance", "stabilize", "resolve", "debug pipeline", "fix workflow"
    ],
    "build": [
        "build", "upgrade", "install", "configure", "compile", "generate", "package",
        "bundle", "setup", "update dependencies", "refactor build", "restructure build", "resolve build issue"
    ],
    "security": [
        "secure", "harden", "encrypt", "sanitize", "patch", "fix", "prevent",
        "validate", "enforce", "strengthen", "protect", "lockdown", "restrict", "authenticate"
    ],
    "revert": [
        "revert", "undo", "rollback", "restore", "reset", "remove",
        "uncommit", "reapply", "discard", "unmerge", "restore previous", "reverse"
    ],
    "deps": [
        "bump", "update", "upgrade", "downgrade", "synchronize", "install",
        "remove", "fix dependency", "resolve conflict", "refresh", "pin version", "patch dependencies"
    ],
    "wip": [
        "draft", "prototype", "experiment", "iterate", "develop", "explore"
    ],
    "release": [
        "release", "deploy", "publish", "tag", "version", "finalize",
        "ship", "prepare", "announce", "mark as stable"
    ],
    "i18n": [
        "translate", "localize", "adapt", "internationalize", "support",
        "convert", "implement i18n", "update locales", "fix translation", "configure language settings"
    ],
    "a11y": [
        "improve", "enhance", "adjust", "enable", "optimize", "refine"
    ],
    "logging": [
        "log", "record", "track", "monitor", "report", "trace"
    ],
    "infra": [
        "deploy", "provision", "configure", "scale", "automate", "manage"
    ]
}

example_commits = {
    "feat": "feat(auth): add OAuth2 with roles\n\nImplemented OAuth2 authentication with role-based access control.",
    "fix": "fix(api): resolve data race issue\n\nFixed concurrency bug by synchronizing access to shared resources.",
    "docs": "docs(api): expand auth docs\n\nUpdated API documentation with authentication flow and error handling details.",
    "refactor": "refactor(core): restructure errors\n\nRemoved redundant code and improved error-handling maintainability.",
    "chore": "chore(deps): upgrade dependencies\n\nUpdated dependency versions to fix vulnerabilities and enhance security.",
    "style": "style(ui): refine button alignment\n\nImproved button positioning for consistent UI layout.",
    "perf": "perf(db): optimize indexing\n\nRefined database indexes to enhance query performance and speed.",
    "test": "test(auth): add OAuth2 tests\n\nImplemented tests to verify OAuth authentication and token management.",
    "build": "build(ci): add Dockerfile\n\nCreated a Dockerfile for consistent application containerization.",
    "ci": "ci(lint): enforce code style\n\nAdded ESLint rules to CI workflow to maintain consistent code quality.",
    "revert": "revert(ui): undo theme changes\n\nReverted recent UI theme changes due to accessibility issues.",
    "security": "security(auth): patch token leakage\n\nFixed issue where expired tokens could be reused under certain conditions.",
    "i18n": "i18n(app): add Spanish translations\n\nIntegrated Spanish language support for multi-language accessibility.",
    "deps": "deps(api): upgrade Django to 4.2\n\nUpdated Django version to latest stable release for security improvements.",
    "wip": "wip(dashboard): redesign analytics page\n\nPartial implementation of analytics dashboard revamp.",
    "release": "release(v1.2.0): prepare for deployment\n\nUpdated changelog and version number for the new release.",
}

commit_training_data = {
    "feat": [
        "feat(api): add JWT authentication\n\nImplemented JWT-based authentication with token expiration and refresh.",
        "feat(ui): support dark mode toggle\n\nAdded a dark mode switch with automatic detection of system preferences.",
        "feat(api): enforce request throttling\n\nImplemented rate limiting to prevent abuse and ensure API stability.",
        "feat(forms): enable live validation\n\nAdded real-time form validation for better user feedback and accuracy.",
        "feat(search): integrate Elasticsearch\n\nBoosted search speed and accuracy by implementing Elasticsearch indexing.",
        "feat(auth): add OAuth2 with role control\n\nImplemented OAuth2 authentication with role-based access restrictions.",
        "feat(notifications): add email alerts\n\nIntroduced automated email notifications for user activity updates.",
        "feat(logging): enhance API logs\n\nAdded structured logging for better error tracking and performance insights.",
        "feat(db): support soft deletes\n\nImplemented soft deletion for records, preserving data while hiding it.",
        "feat(files): support bulk uploads\n\nEnabled bulk file uploads with real-time progress tracking and validation.",
    ],
    "fix": [
        "fix(auth): fix token refresh bug\n\nResolved issue where refresh tokens were not properly invalidated on logout.",
        "fix(api): prevent request deadlocks\n\nOptimized transaction handling to eliminate API request deadlock issues.",
        "fix(security): patch SQL injection\n\nSanitized database queries to mitigate SQL injection vulnerabilities.",
        "fix(ui): fix button alignment issue\n\nCorrected button layout on mobile devices for better UI consistency.",
        "fix(cache): prevent stale data reads\n\nFixed cache invalidation logic to ensure fresh data is always served.",
        "fix(db): fix unique constraint errors\n\nResolved integrity errors caused by duplicate entries in database tables.",
        "fix(notifications): ensure email delivery\n\nFixed issue where email notifications were not being sent reliably.",
        "fix(websockets): fix real-time sync issue\n\nResolved WebSocket desync problem causing delayed chat messages.",
        "fix(auth): prevent session hijacking\n\nStrengthened session management to prevent unauthorized access attempts.",
        "fix(middleware): catch unexpected errors\n\nImproved error handling to prevent crashes from unhandled exceptions.",
    ],
    "docs": [
        "docs(readme): refine setup guide\n\nImproved installation instructions and added common troubleshooting steps.",
        "docs(api): document OAuth2 flow\n\nDetailed OAuth2 integration, token management, and permission scopes.",
        "docs(contrib): update PR guidelines\n\nClarified contribution process, review steps, and merge requirements.",
        "docs(env): document .env config\n\nAdded environment variable documentation for better deployment clarity.",
        "docs(db): improve migration guide\n\nUpdated database migration instructions with rollback and recovery steps.",
        "docs(security): clarify auth flows\n\nDetailed security best practices and authentication flow explanations.",
        "docs(logging): add log format details\n\nProvided logging conventions to ensure consistent debugging insights.",
        "docs(errors): document API error codes\n\nListed API error responses with descriptions for better client handling.",
        "docs(deps): explain dependency versions\n\nClarified dependency requirements and upgrade policies in README.",
    ],
    "refactor": [
        "refactor(auth): modularize auth logic\n\nSeparated authentication logic into modules for better maintainability.",
        "refactor(db): optimize query structure\n\nRewrote complex queries for better performance and readability.",
        "refactor(middleware): unify error handling\n\nStandardized error responses across all middleware layers.",
        "refactor(routes): simplify API paths\n\nReorganized API routes for clarity and consistency across endpoints.",
        "refactor(config): centralize settings\n\nMoved configuration settings to a single file for better manageability.",
        "refactor(models): improve data relations\n\nRefactored database models to optimize relationships and indexing.",
        "refactor(files): clean up temp storage\n\nImproved temporary file management to avoid unnecessary disk usage.",
        "refactor(logging): use structured logs\n\nRefactored logging format to include request details and traceability.",
    ],
    "chore": [
        "chore(deps): upgrade all dependencies\n\nUpdated dependencies to latest stable versions for security and stability.",
        "chore(ci): streamline deployment\n\nOptimized CI/CD workflow to reduce build times and deployment latency.",
        "chore(env): standardize .env file\n\nUpdated environment variable handling for consistency across projects.",
        "chore(build): optimize webpack config\n\nImproved webpack bundling settings to reduce output file size.",
        "chore(ci): enforce linting in pipeline\n\nAdded lint checks to CI workflow to prevent style violations.",
        "chore(release): bump version to 1.2.0\n\nUpdated version number and changelog for the latest release.",
        "chore(deploy): automate staging updates\n\nAdded scripts to auto-deploy updates to the staging environment.",
    ],
    "style": [
        "style(css): unify form styling\n\nApplied consistent padding and border styles to all form fields.",
        "style(lint): enforce ESLint rules\n\nConfigured ESLint to maintain code consistency and best practices.",
        "style(ui): improve navbar spacing\n\nAdjusted spacing for better visual balance across different screen sizes.",
        "style(html): format markup\n\nReformatted HTML files to ensure proper indentation and readability.",
        "style(js): remove unused variables\n\nCleaned up unused JavaScript variables to improve maintainability.",
        "style(tailwind): apply consistent themes\n\nUnified Tailwind themes for better visual consistency across UI.",
    ],
    "perf": [
        "perf(images): enable lazy loading\n\nImplemented lazy loading for images to reduce initial page load time.",
        "perf(db): optimize index usage\n\nRefined database indexing strategy to accelerate query execution speeds.",
        "perf(api): reduce payload size\n\nOptimized API responses by removing redundant data from JSON output.",
        "perf(cache): improve eviction policy\n\nUpdated cache policy to ensure high-priority items remain available.",
        "perf(css): minimize CSS bundle size\n\nReduced CSS file size by eliminating unused styles and improving compression.",
        "perf(worker): parallelize background jobs\n\nOptimized worker processes for faster job execution and resource usage.",
    ],
    "test": [
        "test(auth): add OAuth2 flow tests\n\nAdded integration tests to verify OAuth2 authentication scenarios.",
        "test(api): improve error case coverage\n\nExpanded test cases to cover edge conditions and failure scenarios.",
        "test(forms): validate input constraints\n\nAdded form validation tests to prevent invalid user input submission.",
        "test(cache): add expiration tests\n\nEnsured cached items expire correctly based on defined TTL settings.",
        "test(logging): verify log outputs\n\nTested log messages to ensure they capture correct request details.",
        "test(websockets): simulate real-time load\n\nStress-tested WebSocket connections under high concurrent usage.",
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

VALID_PAIRS = {
    "bl", "br", "ch", "cl", "cr", "dr", "fl", "fr", "gl", "gr",
    "ph", "pl", "pr", "sc", "sh", "sk", "sl", "sm", "sn", "sp",
    "st", "sw", "th", "tr", "tw", "wh", "wr"
}

LETTER_FREQUENCY = {
    "e": 12.7, "t": 9.1, "a": 8.2, "o": 7.5, "i": 7.0,
    "n": 6.7, "s": 6.3, "h": 6.1, "r": 6.0, "d": 4.3,
    "l": 4.0, "c": 2.8, "u": 2.8, "m": 2.4, "w": 2.4,
    "f": 2.2, "g": 2.0, "y": 2.0, "p": 1.9, "b": 1.5,
    "v": 0.98, "k": 0.77, "j": 0.15, "x": 0.15,
    "q": 0.095, "z": 0.074
}