from asyncredisrpc.server import AsyncServer

server = AsyncServer('test_queue', '172.21.17.124')


@server.on_server_start
async def on_server_start():
    print('server start')


@server.task
async def hello():
    print('hello')


@server.task
async def hello2(name):
    print(f'hello, {name}')


if __name__ == '__main__':
    server.run()
