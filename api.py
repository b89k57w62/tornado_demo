from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop

def synshow():
    http_client = HTTPClient()
    response = http_client.fetch("https://ithelp.ithome.com.tw/")

    print(response)
    print("hello，這是同步阻塞的狀況，我已經跟IT邦網站連線了")

async def asynshow():
    http_client = AsyncHTTPClient()
    response = await http_client.fetch("https://ithelp.ithome.com.tw/")
    print(response, "in function")
    print ("hello，這是非同步的狀況，我已經跟IT邦網站連線了")


synshow()
# loop = IOLoop.current()

# loop.run_sync(asynshow)