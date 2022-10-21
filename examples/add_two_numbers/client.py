import asyncio
from asyncredisrpc.client import AsyncClient


async def main():
    queue_name = 'test_queue'
    client = AsyncClient(queue_name, '172.21.16.114')
    await client.connect()
    ret, data = await client.call('sum', 14, 3)
    print(f'get result: {ret} {data}')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
