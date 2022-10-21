import asyncio

from asyncredisrpc.client import AsyncClient

client = AsyncClient('test_queue', '172.21.16.114')


async def main():
    await client.connect()
    ret, data = await client.call('hello')
    print(f'hello result: {ret} {data}')
    ret, data = await client.call('hello2', 'world')
    print(f'hello2 result: {ret} {data}')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())