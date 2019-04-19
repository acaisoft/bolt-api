import logging
import os

from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from services import const


def configure(app: Flask):
    # common flask app configuration
    app.logger.setLevel(logging.DEBUG if app.debug else logging.INFO)

    conf_file_path = os.environ.get('CONFIG_FILE_PATH', 'localhost-config.py')
    app.config.from_pyfile(conf_file_path)

    secrets_file_path = os.environ.get('SECRETS_FILE_PATH', 'localhost-secrets.py')
    app.config.from_pyfile(secrets_file_path)

    sentry_dsn = app.config.get('SENTRY_DSN', None)
    if sentry_dsn and not app.debug:
        logging.info(f'sentry logging to {sentry_dsn.split("@")[-1]}')
        sentry_sdk.init(sentry_dsn, integrations=[FlaskIntegration()])

    config_ver = app.config.get('CONFIG_VERSION', None)
    secrets_ver = app.config.get('SECRETS_VERSION', None)

    app.logger.info(f'app configured using {conf_file_path} v{config_ver} and {secrets_file_path} v{secrets_ver}')


def validate(app, required_config_vars):
    missing = []
    for var_name in required_config_vars:
        if not app.config.get(var_name):
            missing.append(var_name)
    assert not missing, f'{len(missing)} undefined config variables: {", ".join(missing)}'
    app.logger.info('config valid')