import asyncio

async def handle_request(reader, writer):
    print('handling request')
    data = await reader.read(1024)
    content = data.decode('utf-8')

    addr = writer.get_extra_info('peername')
    print('received', content, 'from', addr)

    print('send hello world')
    writer.write(b'''HTTP/1.1 200 OK\r\n\r\nHello World!''')
    await writer.drain()

    print('close socket')
    writer.close()


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_request, host='0.0.0.0', port=8000, loop=loop)
server = loop.run_until_complete(coro)

print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
