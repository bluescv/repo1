import www.orm
from www.models import User
import asyncio

loop = asyncio.get_event_loop()


async def test():
    # yield from www.orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    await www.orm.create_pool(loop, user='www-data', password='www-data', db='awesome')

    # u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')

    await u.save()


print('ormtest start')
loop.run_until_complete(test())
