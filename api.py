from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

def synshow():
    http_client = HTTPClient()
    response = http_client.fetch("https://ithelp.ithome.com.tw/")

    print(response)
    print("sync issue, connected successfully.")

async def asynshow():
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("https://ithelp.ithome.com.tw/")
    print(response, "in function")
    print ("async issue, connected successfully.")


synshow()
# loop = IOLoop.current()

# loop.run_sync(asynshow)