import falcon

from random import randint

from template_set import render


class HelloResource(object):
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.content_type = 'text/html; charset=utf-8'
        response.body = render('main.html', world=randint(1, 9999))


app = falcon.API()

app.add_route('/', HelloResource())
