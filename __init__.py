from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
    config = Configurator()
    config.scan("file")

    config.add_route('line_chart', '/line_chart')
    config.add_route('scatter_plot', '/scatter_plot')
    config.add_route('pie_chart', '/pie_chart')
    config.add_route('bar_chart', '/bar_chart')
    config.add_route('histogram', '/histogram')
    config.scan("loadfile_matplotlib")
    config.add_route('load_file_matplotlib', '/load_file_matplotlib')
    config.scan("from_internet")
    config.add_route('from_internet', '/from_internet')
    app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 8080, app)
    server.serve_forever()