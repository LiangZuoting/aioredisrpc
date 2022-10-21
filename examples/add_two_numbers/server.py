import asyncio
from src.server import AsyncServer

queue_name = 'test_queue'
server = AsyncServer(queue_name, '172.21.16.114')


@server.task
async def sum(x, y):
    print('summing...')
    await asyncio.sleep(1)
    return x + y


if __name__ == '__main__':
    server.run()
