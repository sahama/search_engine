from pyramid.view import view_config
import pyramid_bowerstatic
import os

components = pyramid_bowerstatic.create_components('search_engine',
                                                   os.path.join(os.path.dirname(__file__), 'static',
                                                                'bower_components'))


@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view(request):
    request.include(components, 'bootstrap')
    request.include(components, 'jquery')

    return {'project': 'search_engine'}
