from src.server import AsyncServer

server = AsyncServer('test_queue', '172.21.16.114')


@server.task
async def hello():
    print('hello')


@server.task
async def hello2(name):
    print(f'hello, {name}')


if __name__ == '__main__':
    server.run()
