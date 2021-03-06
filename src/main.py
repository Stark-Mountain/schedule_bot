from pathlib import Path

import asyncio
from aiohttp import web
from aiopg.sa import create_engine
from sqlalchemy.engine.url import URL

from .bots.tg import register
from .settings import Settings
from .views import index
from .middlewares import middlewares


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


def setup_bots(app):
    # TODO
    tokens = []
    for token in tokens:
        bot = register(token)
        loop = asyncio.get_event_loop()
        app['bots'] = loop.create_task(bot.loop())


async def create_app():
    app = web.Application(middlewares=middlewares)
    settings = Settings()
    app.update(
        name='test',
        settings=settings
    )

    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)

    setup_routes(app)

    setup_bots(app)

    return app
