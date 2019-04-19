from healthcheck import HealthCheck, EnvironmentDump

from services.cache import get_cache
from services.hasura import hasura_client, hce


def register_app(app):

    hc = HealthCheck(app, '/healthcheck')

    if app.debug:
        EnvironmentDump(app, '/env')

    def redis_up():
        info = get_cache(app.config).info()
        return True, 'ok'

    def hasura_up():
        client = hasura_client(app.config)
        try:
            response = hce(app.config, 'query { user { id } }')
        except Exception as e:
            return False, str(e)
        if not response.get('user', None):
            return False, 'missing root tables'
        return True, 'ok'

    def deployer_up():
        try:
            response = app.services.deployer.clients.healthcheck(app.config).health_check_get()
        except Exception as e:
            return True, str(e)
        if response.status != 'healthy':
            return True, f'deployer is not healthy, it is {response.status}'
        return True, 'ok'

    hc.add_check(redis_up)
    # hc.add_check(hasura_up)
    hc.add_check(deployer_up)

    return hc