from jinja2 import Environment, FileSystemLoader


def render(page, **kwargs):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(page)
    return template.render(**kwargs)
