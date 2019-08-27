import falcon
from random import randint


class ThingsResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = (f'Hello,fucking world Nº {randint(1, 9999)}!')


app = falcon.API()

things = ThingsResource()

app.add_route('/', things)
