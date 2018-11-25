# import sys

# from aiohttp import web

# from src.db import close_pg, init_pg
# from src.settings import get_config
# from src.routes import setup_routes
# from src.middlewares import setup_middlewares


# async def init_app(argv=None):

#     app = web.Application()

#     app['config'] = get_config(argv)

#     # setup Jinja2 template renderer
#     aiohttp_jinja2.setup(
#         app, loader=jinja2.PackageLoader('aiohttpdemo_polls', 'templates'))

#     # create db connection on startup, shutdown on exit
#     app.on_startup.append(init_pg)
#     app.on_cleanup.append(close_pg)

#     # setup views and routes
#     setup_routes(app)

#     setup_middlewares(app)

#     return app


# async def main(argv):

#     app = init_app(argv)

#     config = get_config
#     web.run_app(app,
#                 host=config['host'],
#                 port=config['port'])


# if __name__ == '__main__':
#     # FIXME: parse args as normal human
#     main(sys.argv[1:])

from pathlib import Path

from aiohttp import web
from aiopg.sa import create_engine
from sqlalchemy.engine.url import URL

from .settings import Settings
from .views import index, message_data, messages


THIS_DIR = Path(__file__).parent
BASE_DIR = THIS_DIR.parent


def pg_dsn(settings: Settings) -> str:
    """
    :param settings: settings including connection settings
    :return: DSN url suitable for sqlalchemy and aiopg.
    """
    return str(URL(
        database=settings.DB_NAME,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        username=settings.DB_USER,
        drivername='postgres',
    ))


async def startup(app: web.Application):
    app['pg_engine'] = await create_engine(pg_dsn(app['settings']), loop=app.loop)


async def cleanup(app: web.Application):
    app['pg_engine'].close()
    await app['pg_engine'].wait_closed()


def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_route('*', '/messages', messages, name='messages')
    app.router.add_get('/messages/data', message_data, name='message-data')


async def create_app():
    app = web.Application()
    settings = Settings()
    app.update(
        name='test',
        settings=settings
    )

    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)

    setup_routes(app)
    return app
