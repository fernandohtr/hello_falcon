import falcon
from random import randint


class HelloResource(object):
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = (f'Ricky diz: "Hello, world Nº {randint(1, 9999)}!"')


app = falcon.API()

hello = HelloResource()

app.add_route('/', hello)
