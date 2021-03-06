Changelog
=========

## 0.2.9 (2019-05-29)

### Changes

* Switch from notification-based to handler-based image processing. [Piotr Mońko]

* Add default metrics charts configuration. [Piotr Mońko]

* Add monitoring interval parameter. [Piotr Mońko]

* Return token from testrun_start if role is ADMIN. [Piotr Mońko]

* Add tenant_admin role support, add scenario params deployer support, bump deployer version, add debug token output from testrun_start. [Piotr Mońko]

* Make conf params required only when load_tests scenario is enabled. [Piotr Mońko]

### Other

* Add tests. [Piotr Mońko]

* Add more vcr tests. [Piotr Mońko]

* Add testutil and projec tests. [Piotr Mońko]

* Add exec_id to insert of totals. [Piotr Mońko]

* Fix requests totals query. [Piotr Mońko]

* Optimize and reduce heavy callbacks. [Piotr Mońko]

* Optimize and reduce heavy callbacks. [Piotr Mońko]

* Remove retalimiting from webhooks. [Piotr Mońko]

* Add missing requirement. [Piotr Mońko]

* Merge branch 'master' into bup. [Piotr Mońko]

* Fix typo in hasura permissions, add ratelimiting to webhooks. [Piotr Mońko]

* Remove worker-tmp-dir. [Piotr Mońko]

* Merge branch 'master' into bup. [Piotr Mońko]

* Fix another type. [Piotr Mońko]

* Fix type. [Piotr Mońko]

* Add configuration chart metadata. [Piotr Mońko]

* Change gunicorn worker-tmp-dir. [Piotr Mońko]

* Fix missing input wrapper. [Piotr Mońko]

* Merge branch 'master' into bup. [Piotr Mońko]

* Implement bolt uploads processor. [Piotr Mońko]

* Fix bad code. [Piotr Mońko]

* Fix pip requirements. [Piotr Mońko]

* Fix project summary additional fields. [Piotr Mońko]

* Add migrations for monitoring_interval. [Piotr Mońko]

* Fix validation configuration updataion. [Piotr Mońko]

* Fix quiet update error. [Piotr Mońko]

* Validate testrun has_something. [Piotr Mońko]

* Remove temporarily new constant. [Piotr Mońko]

* Update bolt-deployer. [Piotr Mońko]

* Add new param. [Piotr Mońko]

* Fix perms. [Piotr Mońko]

* Fix build. [Piotr Mońko]

* Change perms in metadata. [Piotr Mońko]

* Remove invalid update. [Piotr Mońko]

* Fix missing return. [Piotr Mońko]

* Fix missing return. [Piotr Mońko]

* Increase worker timeout, add workers, fix bytes>int comparison. [Piotr Mońko]

* Track upserts. [Piotr Mońko]

* Add logs. [Piotr Mońko]

* Add logs. [Piotr Mońko]

* Merged in refactoring-requirements (pull request #16) [Artiom Borysiewicz]

  Refactoring

* Refactoring. [art.barysevich]

* Merged in refactoring-requirements (pull request #15) [Artiom Borysiewicz]

  Fix pip. Refactoring

* Fix pip. Refactoring. [art.barysevich]

* Update bolt-deployer sdk, add charts conf data storage table. [Piotr Mońko]

* Rename types in configuration create/update. [Piotr Mońko]

* Convert mounts_per_worker to int. [Piotr Mońko]

* Fix type mismatch. [Piotr Mońko]

* Add configuration sections support. [Piotr Mońko]

* Increase deployer connection timeout. [Piotr Mońko]

* Refactor export endpoints. add raw json output. [Piotr Mońko]


## 0.2.8 (2019-05-10)

### Changes

* Change TESTRUN_MAX_USERS_PER_INSTANCE to 690. [Piotr Mońko]

* Add envvars manipulations to testrun_configuration_update mutation. [Piotr Mońko]

### Other

* Add domain to export link. [Piotr Mońko]

* Fix timestamp conversion error. [Piotr Mońko]

* O Merge branch 'extensions_data_exports' [Piotr Mońko]

* Fix lost order. [Piotr Mońko]

* Merged in extensions_data_exports (pull request #14) [Piotr Mońko]

  wip nfs extension data in exports

* Wip nfs extension data in exports. [Piotr Mońko]

* Add nfs additional data series support to exporter. [Piotr Mońko]

* Merged in add-slug-and-created-at-to-additional-data (pull request #13) [Artiom Borysiewicz]

  Add slug/created_at to additional data

* Fix migrations. [art.barysevich]

* Add slug/created_at to additional data. [art.barysevich]

* Fix return invalid column type in tabular data export. [Piotr Mońko]

* Fix data exporter to use new execution_errors table. [Piotr Mońko]

* Change identifier to query name in exported data. [Piotr Mońko]

* Fix output of testrun_project_summary. [Piotr Mońko]

* Update test runner version. [Piotr Mońko]

* Add min_/max_ from avg resp size to request_totals. [Piotr Mońko]

* Fix minor issues. [Piotr Mońko]

* Merged in add-execution-id-for-testrunner-permissions (pull request #12) [Artiom Borysiewicz]

  Add permissions for execution_id for testrunner

* Add permissions for execution_id for testrunner. [art.barysevich]

* Add update and update_validate extension mutations. [Piotr Mońko]

* Update testrunner version, add create and create_validate mutations to extensions. [Piotr Mońko]

* Merged in add-table-with-additional-data (pull request #11) [Artiom Borysiewicz]

  Add table with additional data

* Add table with additional data. [art.barysevich]

* Update version. Update docker-compose file for mac. [art.barysevich]

* Update image version 0.1.17 -> 0.1.18. [art.barysevich]

* Fix error. [Piotr Mońko]

* Bump test runner version. [Piotr Mońko]

* Add nfs extension support to db and deployer. [Piotr Mońko]

* Remove total calculations on delete. [Piotr Mońko]

* Increase worker timeout. [Piotr Mońko]

* Increase worker timeout. [Piotr Mońko]

* Fix asserts in hasura webhooks. [Piotr Mońko]

* Bump test runner version. [Piotr Mońko]

* Cleanup unused tables, fix crash. [Piotr Mońko]


## 0.2.7 (2019-04-29)

### Changes

* Add envvars manipulations to testrun_configuration_update mutation. [Piotr Mońko]

* Add requests and distributions details. [Piotr Mońko]

* Add testrunner env variables to configuration create mutation. [Piotr Mońko]

* Add testrunner env variables to configuration create mutation. [Piotr Mońko]

* Add support for table extractors for data export/grafana and enable mixed-mode (series+table) output. [Piotr Mońko]

### Fix

* Configuration update error. [Piotr Mońko]

### Other

* Add backend webhook to calculate totals for requests. [Piotr Mońko]

* Decrease throttling on data export; bump test runner version. [Piotr Mońko]

* Fix input type changed in hasura beta44. [Piotr Mońko]

* Fix validated type. [Piotr Mońko]

* Adjust exporter to match new requests distributions. [Piotr Mońko]

* Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr Mońko]

* Fix bolt-metrics-api chart. [jroslaniec-acaisoft]

* Add volumne for grafana. [Piotr Mońko]

* Add command and debugging flask app: [Piotr Mońko]

* Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr Mońko]

* Mount config voluems for bolt-metrics-api chart. [jroslaniec-acaisoft]

* Add bolt-metrics-api chart. [jroslaniec-acaisoft]

* Add metrics-api building process to Jenkinsfile. [jroslaniec-acaisoft]

* Migrations. [Piotr Mońko]

* Fix gunicorn params. [Piotr Mońko]

* Fix gunicorn params. [Piotr Mońko]

* Update Jenkinsfile. [Piotr Mońko]

* Update changelog. [Piotr Mońko]


## 0.2.6 (2019-04-19)

### Changes

* Bump test-runner version, add delete perm to manager. [Piotr Mońko]

* Add number of users to result aggregate. [Piotr Mońko]

* Allow manager to do aggregation requests on configuration and execution. [Piotr Mońko]

* Add testrun_project_summary endpoint. [Piotr Mońko]

* Adjust smoke test project. [Piotr Mońko]

* Adjust smoketest and validation parameters. [Piotr Mońko]

### Other

* Update changelog. [Piotr Mońko]

* Wip: refactor to split into multiple api servers and common services. [Piotr Mońko]

* Fix returned fields. [Piotr Mońko]

* Add missing testrun_conf_delete. [Piotr Mońko]

* Bump test-runner version. [Piotr Mońko]

* Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr Mońko]

* Update version of image for test runner. [art.barysevich]

* Merge branch 'prod' [Piotr Mońko]

* Increase maximum simultaneous users limit to 30000. [Piotr Mońko]

* Adjust mock repo hostname. [Piotr Mońko]

* Update permissiong. [Piotr Mońko]

* Fix workers/instances. [Piotr Mońko]

* Add soft-deletion support. [Piotr Mońko]

* Add db support for is_deleted flag. [Piotr Mońko]

* Merged in update-version-of-image-0.1.6 (pull request #9) [Artiom Borysiewicz]

  Update version of image 0.1.6

* Update version of image 0.1.6. [art.barysevich]

* Update changelog. [Piotr Mońko]


## 0.2.5 (2019-04-08)

### Fix

* Fix slow repository validation, fix invalid error message (caused by timeouts), fix openapi sdk errors with headers returned to users. [Piotr Mońko]

### Other

* Update bolt-deployer. [Piotr Mońko]

* Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr Mońko]

* Add release env var to docker image. [jroslaniec-acaisoft]

* Move demo setup to thread. [Piotr Mońko]

* Add logging to debugging. [Piotr Mońko]

* Add cache to deployer repository validation. [Piotr Mońko]

* Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr Mońko]


## 0.2.4 (2019-04-04)

### Changes

* Add user creation/registration mutation. [Piotr Mońko]

* Update configuration.instances on configuration param change. [Piotr Mońko]

### Other

* Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr Mońko]

* Add docker-compose file for mac. [art.barysevich]

* Add user and user roles management mutations and commands. [Piotr Mońko]


## 0.2.3 (2019-04-02)

### Changes

* Update configuration.instances on configuration param change. [Piotr Mońko]

* Add permissions for testrunner role. [Piotr Mońko]

* Add loucst_start and _end columns. [Piotr Mońko]

* Bump test runner image to v0.1.3. [Piotr Mońko]

### Other

* Make deployer outage non-fatal. [Piotr Mońko]

* Remove secret. [Piotr Mońko]

* Remove secret. [Piotr Mońko]

* Use selfsigned testrunner token in debug mode. [Piotr Mońko]

* Fix bad import. [Piotr Mońko]

* Rename 'creator' to 'test_creator' [Piotr Mońko]

* Tagged release. [Piotr Mońko]


## 0.2.2 (2019-03-28)

### Changes

* Refactor job status. [Piotr Mońko]

* Adjusted permissions. [Piotr Mońko]

* Change test_creator create and add update methods. [Piotr Mońko]

* Add test_source creation on repository creation. [Piotr Mońko]

### Fix

* Fix empty name not required on repo update. [Piotr Mońko]

### Other

* Updated test runner image. [Piotr Mońko]

* Add MOCK_REPO support. [Piotr Mońko]

* Merge branch 'refactor_out_the_m2m' [Piotr Mońko]


## 0.2.1 (2019-03-27)

### Changes

* Changed repository and creator relations to configuration to go through test_source. [Piotr Mońko]

* Delete test_creator_m2m table. [Piotr Mońko]

* Increase deployer service connection timeout setting. [Piotr Mońko]

### Other

* Merge branch 'refactor_out_the_m2m' [Piotr Mońko]

* Update changelog. [Piotr Mońko]


## 0.2.0 (2019-03-27)

### Changes

* Change how job status is reported for an image testrun. [Piotr Mońko]

### Fix

* Add back configuration creation parameters validation. [Piotr Mońko]

### Other

* Fix full token to auth token. [Piotr Mońko]

* Set default BOLT_TEST_RUNNER_IMAGE. [Piotr Mońko]


## 0.1.9 (2019-03-27)

### Changes

* Update demo project seed. [Piotr Mońko]

* Change testrunner authentication mechanism. [Piotr Mońko]

### Fix

* Add back configuration creation parameters validation. [Piotr Mońko]


## 0.1.8 (2019-03-27)

### Changes

* Change testrunner authentication mechanism. [Piotr Mońko]

* Add back image_url to project_create endpoint. [Piotr Mońko]

* Move upload endpoints to a generic method. [Piotr Mońko]

* Populate execution_id fields in execution results tables from testrunner role id. [Piotr Mońko]

* Remove image_url from project create method. [Piotr Mońko]

### Fix

* Fix demo seed for result_distribution. [Piotr Mońko]

* Fix nonserializable bytes error. [Piotr Mońko]

### Other

* Switch job token to keycloack. [Piotr Mońko]

* Limit logging graphql exceptions, wip. [Piotr Mońko]

* Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr Mońko]

* Merged in add-on-start-and-on-stop (pull request #8) [Artiom Borysiewicz]

  Add on start and on stop

* Add tests for models. [art.barysevich]

* Add tests for models. [art.barysevich]

* Add tests for models. [art.barysevich]

* Test commit. [art.barysevich]


## 0.1.7 (2019-03-25)

### Changes

* Remove image_url from project create method. [Piotr Mońko]

* Add validation and authorization for testrunner process. [Piotr Mońko]

* Update bolt-deployer. [Piotr Mońko]

* Add permissions for testrunner role. [Piotr Mońko]

* Added test_sources table, adjusted relations and code. [Piotr Mońko]

### Fix

* Fix test_source seed. [Piotr Mońko]

* Fix unresolvable slug_name in testrun configuration validation. [Piotr Mońko]

### Other

* Fix configuration update param value. [Piotr Mońko]


## 0.1.6 (2019-03-22)

### Changes

* Remove image_url filetype validation on project. [Piotr Mońko]

### Fix

* Fix unresolvable slug_name in testrun configuration validation. [Piotr Mońko]

* Fix load_tests_host slug. [Piotr Mońko]

* Fix typo in configuration_create. [Piotr Mońko]


## 0.1.5 (2019-03-21)

### Changes

* Remove image_url filetype validation on project. [Piotr Mońko]

### Other

* Update changelog. [Piotr Mońko]


## 0.1.4 (2019-03-21)

### Changes

* Add demo project setup and teardown mutations. [Piotr Mońko]

* Switch parameters to slug_names, follow with relations. [Piotr Mońko]

* Allow change to repository url if not yet performed. [Piotr Mońko]

### Fix

* Fix repository name/url validation. [Piotr Mońko]

* Fix project without access error message. [Piotr Mońko]

* Fix signed url upload method. [Piotr Mońko]

### Other

* Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr Mońko]

* Add GOOGLE_APPLICATION_CREDENTIALS env var to deployment. [jroslaniec-acaisoft]

* Enable type_slug edition. [Piotr Mońko]

* Add create/_validate and update/_validate methods for repository. [Piotr Mońko]


## 0.1.3 (2019-03-20)

### Changes

* Add testrun_project_image_upload implementation. [Piotr Mońko]

* Refactor hasura connection names. [Piotr Mońko]

### Fix

* Fix some non-camelcase hasura relation names. [Piotr Mońko]

### Other

* Add create/_validate and update/_validate methods for repository. [Piotr Mońko]

* Update changelog. [Piotr Mońko]


## 0.1.2 (2019-03-18)

### Changes

* Add common Interface for typed schema responses. [Piotr Mońko]

* Add testrun_project_image_upload stub method placeholder. [Piotr Mońko]

* Wrap project_create and configuration_create in ReturnTypes with .returning members. [Piotr Mońko]

* Rename configurationParams relation to configuration_params. [Piotr Mońko]

### Other

* Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr Mońko]

* Add testrun_project_image_upload stub method placeholder. [Piotr Mońko]

* Update changelog. [Piotr Mońko]

* Add testrun_project_create and testrun_project_create_validate. [Piotr Mońko]

* Change: rename configurationParams relation on configuration to configuration_params. [Piotr Mońko]


0.1.0 (2019-03-15)
-------------------
- Update readme. [Piotr Mońko]
- Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr
  Mońko]
- Delete bolt_api catalog from Dockerfile. [art.barysevich]
- Merged in refactoring-test-creator (pull request #7) [Artiom
  Borysiewicz]

  Refactoring Test Creator
- Configuration update endpoints. [Piotr Mońko]
- Change test_creator to match by m2m. [Piotr Mońko]
- Merged in validation-for-test-creator (pull request #6) [Artiom
  Borysiewicz]

  Add validators for TestCreator
- Add validators for TestCreator. [art.barysevich]
- Test_creator validations. [Piotr Mońko]
- Add scaffold for test_creator graphql mutation, add test_creator
  table. [Piotr Mońko]
- Record commit_hash. [Piotr Mońko]
- Fix invalid key. [Piotr Mońko]
- Handle multiple auth id in hasura. [Piotr Mońko]
- Fix invalid import. [Piotr Mońko]
- Add repository connectivity test at validation time. [Piotr Mońko]
- Add no_cache. [Piotr Mońko]
- Update bolt-deployer version, add performed flag -check. [Piotr Mońko]
- Fix CRASHED in testrun status. [Piotr Mońko]
- Setup update testrun_status callback. [Piotr Mońko]
- Fix nonrefreshing schema. [Piotr Mońko]
- Upgrade from raven to sentrysdk. [Piotr Mońko]
- Add sentry_check command. [Piotr Mońko]
- Add test job error to execution, fix job status. [Piotr Mońko]
- Add project validators, refactor configuration validators. [Piotr
  Mońko]
- Fix missing requirement. [Piotr Mońko]
- Fix invalid gitmodule. [Piotr Mońko]
- Delete users table. [Piotr Mońko]
- Remove job status return value for running tests. [Piotr Mońko]
- Allow admin to start any configurateion testrun. [Piotr Mońko]
- Allow admin to start any configurateion testrun. [Piotr Mońko]
- Use only first role. [Piotr Mońko]
- Remove user id validation for testing. [Piotr Mońko]
- Remove hasura endpoint. [Piotr Mońko]
- Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr
  Mońko]
- Refactor helm chart and jenkinsfile. #DO-51. [Kamil Litwiniuk]
- Describe DEMO steps. [Piotr Mońko]
- Fix migrations. [Piotr Mońko]
- Remove teporarily configuration insertion. [Piotr Mońko]
- Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr
  Mońko]
- Merged in refactoring-graphql-queries (pull request #4) [Artiom
  Borysiewicz]

  Refactoring. Add tests for serializing data
- Merge from master. [art.barysevich]
- Refactoring. Add tests for serializing data. [art.barysevich]
- Update config. [jroslaniec-acaisoft]
- Fix - Decrypt secrets in Jenkins. [jroslaniec-acaisoft]
- Fix secrets. [jroslaniec-acaisoft]
- Add unified status interface, add consolidated configuration
  validation. [Piotr Mońko]
- Add config and secret versions. [Piotr Mońko]
- Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr
  Mońko]
- Revert "Revert "Revert "Change submodule to https""" [jroslaniec-
  acaisoft]

  This reverts commit 3af5a42e3a719b666785749eb0531052856d09d0.
- Revert "Revert "Change submodule to https"" [jroslaniec-acaisoft]

  This reverts commit 4fdcf9f85aae621d02b064195931ec5735e81f58.
- Revert "Change submodule to https" [jroslaniec-acaisoft]

  This reverts commit 6fd95cb87ae2f5a814a3eeac44aa167047d8620f.
- Change submodule to https. [jroslaniec-acaisoft]
- Add logging. [Piotr Mońko]
- Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr
  Mońko]
- Update submodule user. [jroslaniec-acaisoft]
- Add dev deployment to k8s. [jroslaniec-acaisoft]
- Remove personal id. [Piotr Mońko]
- Add endpoint for obtaining key, checking job status. [Piotr Mońko]
- Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr
  Mońko]
- Add default type_id to repository. [mateuszbernat]
- Add configuration type relation to repository. [mateuszbernat]
- Removed username and password fields from repository table, added
  performed field to repository and configurations tables.
  [mateuszbernat]
- Add bolt_deployer healthcheck. [Piotr Mońko]
- Moved type from configurations to repositories. [mateuszbernat]
- Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Piotr
  Mońko]
- Add REDIS_PASS to secrets. [jroslaniec-acaisoft]
- Add redis password. [Piotr Mońko]
- Fix imports. [Piotr Mońko]
- Merge branch 'acbt-26-start-test' [Piotr Mońko]
- Refactor configuration. [Piotr Mońko]
- Merge remote-tracking branch 'origin/master' into acbt-26-start-test.
  [Piotr Mońko]
- Refs #acbt-26. wip. [Piotr Mońko]
- Add helm chart. [jroslaniec-acaisoft]
- Add Jenkinsfile. [jroslaniec-acaisoft]
- Merged in fix-upstreams-and-api-client (pull request #3) [Artiom
  Borysiewicz]

  Fix arguments for upstreams. Modify client for bolt-api. Fix fields
- Fix arguments for upstreams. Modify client for bolt-api. Fix fields.
  [art.barysevich]
- Add permissions and more tables. [Piotr Mońko]
- Refactor some column names. [Piotr Mońko]
- Remove leftovers. [Piotr Mońko]
- Add example instance configuration. [Piotr Mońko]
- Some updates. [Piotr Mońko]
- Fix double handler. [Peter Monko]
- Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Peter
  Monko]
- Merged in add-result-error-table (pull request #2) [Artiom
  Borysiewicz]

  Add result_error table, migrations and function for client
- Add result_error table, migrations and function for client.
  [art.barysevich]
- Add permissions again. [Peter Monko]
- Add permissions. [Peter Monko]
- Refactor structure. [Peter Monko]
- Merged in api-client (pull request #1) [Artiom Borysiewicz]

  Add python client for bolt api
- Add python client for bolt api. [art.barysevich]
- Remote schema poc. [Piotr Mońko]
- Change uwsgi to gunicorn. [Piotr Mońko]
- Add result_distribution and helpers. [Piotr Mońko]
- Add user, project, conf views. [Peter Monko]
- Merge branch 'master' of bitbucket.org:acaisoft/bolt-api. [Peter
  Monko]
- Add more upstreams. [Piotr Mońko]
- Add result aggregate. [Piotr Mońko]
- Add bare hasura dockerfile. [Peter Monko]
- Add python requirements. [Peter Monko]
- Initial. [Peter Monko]


