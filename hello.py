import falcon

from jinja2 import Environment, FileSystemLoader
from random import randint


class HelloResource(object):
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.content_type = 'text/html'

        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        template = env.get_template('main.html')

        response.body = template.render(world=randint(1, 9999))


app = falcon.API()

hello = HelloResource()

app.add_route('/', hello)
