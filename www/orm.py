# orm for database
import asyncio, logging

import aiomysql


async def create_pool(loop, **kwargs):
    logging.info('creating database connection pool ...')
    global _pool
    _pool = await aiomysql.create_pool(
        host=kwargs.get('host', 'localhost'),
        port=kwargs.get('port', 3306),
        user=kwargs['pyuser'],
        password=kwargs['pyuser'],
        db=kwargs['db'],
        charset=kwargs.get('charset', 'utf8'),
        autocommit=kwargs.get('autocommit', True),
        maxsize=kwargs.get('maxsize', 10),
        minsize=kwargs.get('minsize', 1),
        loop=loop
    )
