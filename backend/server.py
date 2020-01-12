from aiohttp import web


async def ping(request):
    return web.json_response(data={'status': 'ok'})


def main():
    app = web.Application()
    app.add_routes([web.get('/ping', ping)])
    return app


if __name__ == '__main__':
    app = main()
    web.run_app(app)