SECRET_KEY = 'SECRET_KEY'
JWT_ALGORITHM = 'JWT_ALGORITHM'
HASURA_CLIENT_USER_ID = '7f1aab7a-e941-46a2-b63a-5b28b80ad384'

ROLE_ADMIN = 'admin'
ROLE_MANAGER = 'manager'
ROLE_TESTER = 'tester'
ROLE_READER = 'reader'
ROLE_TESTRUNNER = 'testrunner'  # internal use
ROLE_CHOICE = (ROLE_ADMIN, ROLE_MANAGER, ROLE_TESTER, ROLE_READER)

TENANT_ID = '1'

TESTRUN_INIT = 'INIT'
TESTRUN_PREPARING = 'PENDING'
TESTRUN_PREPARING_FAILED = 'PREPARING FAILED'
TESTRUN_STARTED = 'STARTED'
TESTRUN_RUNNING = 'RUNNING'
TESTRUN_CRASHED = 'CRASHED'
TESTRUN_FINISHED = 'FINISHED'

TESTTYPE_LOAD = 'load_tests'
TESTTYPE_CHOICE = (TESTTYPE_LOAD,)

TESTPARAM_USERS = 'load_tests_users'
TESTRUN_MAX_USERS_PER_INSTANCE = 2000
TESTRUN_MAX_USERS = 30000
TESTRUN_MAX_DURATION = 1800

CONF_SOURCE_JSON = 'test_creator'
CONF_SOURCE_REPO = 'repository'
CONF_SOURCE_CHOICE = (CONF_SOURCE_JSON, CONF_SOURCE_REPO)

IMAGE_CONTENT_TYPES = ('image/png', 'image/jpg', 'image/jpeg', 'image/gif')
UPLOADS_MAX_SIZE_BYTES = 5000000

REQUIRED_BOLT_API_CONFIG_VARS = (
    'KEYCLOAK_URL',
    'KEYCLOAK_CLIENT_ID',
    'KEYCLOAK_REALM_NAME',
    'KEYCLOAK_CLIENT_SECRET',
    'HASURA_GQL',
    'HASURA_GRAPHQL_ACCESS_KEY',
    'BOLT_DEPLOYER_ADDR',
    'BOLT_DEPLOYER_TOKEN',
    # 'BOLT_TEST_RUNNER_IMAGE',
    'REDIS_HOST',
    'REDIS_PORT',
    'REDIS_DB',
    'BUCKET_PUBLIC_UPLOADS',
    'SECRET_KEY',
)

REQUIRED_METRICS_API_CONFIG_VARS = (
    'HASURA_GQL',
    'HASURA_GRAPHQL_ACCESS_KEY',
    'REDIS_HOST',
    'REDIS_PORT',
    'REDIS_DB',
    'SECRET_KEY',
)

# default testrunner image for use by `test_creator` tests, override with BOLT_TEST_RUNNER_IMAGE
DEFAULT_TEST_RUNNER_IMAGE = 'eu.gcr.io/acai-bolt/bolt-test-runner:0.1.29'

# allows load tests setup/teardown to work without getting ratelimited by repository hosting
MOCK_REPOSITORY = 'git@mockbitbucket.org:repo'

DATA_EXPORT_TOKEN_HANDLE_ID = 'oid'
EXPORT_SCOPE_PROJECT = 'project'
EXPORT_SCOPE_EXECUTION = 'execution'
EXPORT_SCOPE_CHOICE = (EXPORT_SCOPE_PROJECT, EXPORT_SCOPE_EXECUTION)

# configuration extensions
EXTENSION_NFS = 'nfs'
EXTENSION_CHOICE = (EXTENSION_NFS,)
