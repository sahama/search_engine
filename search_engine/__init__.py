from pyramid.config import Configurator
import os
pkg_root = os.path.abspath(os.path.dirname(__file__))
pkg_location = os.path.abspath(os.path.dirname(pkg_root))

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_bowerstatic')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
