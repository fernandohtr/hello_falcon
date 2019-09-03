from jinja2 import Environment, FileSystemLoader


def render(page, **kwargs):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(page)
    
    for key, value in kwargs.items():
        key = key
        value = value

    return template.render(key=value)
