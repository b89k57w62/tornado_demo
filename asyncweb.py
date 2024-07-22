from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("https://ithelp.ithome.com.tw/") 
        if response.error:
            raise tornado.web.HTTPError(500)

        self.write(response.body)

def my_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler)
        ]
    )

def main():
    app = my_app()
    app.listen(8888)
    IOLoop.current().start()

if __name__ == "__main__":
    main()
