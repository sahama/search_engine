from pyramid.view import view_config
import pyramid_bowerstatic
import os
import re
import operator

import urllib.parse

from .reverse_index import create
reverse_index, page_index = create()
modified_page_index = [urllib.parse.unquote(url) for url in page_index]

components = pyramid_bowerstatic.create_components('search_engine',
                                                   os.path.join(os.path.dirname(__file__), 'static',
                                                                'bower_components'))


@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view(request):
    results = {}
    request.include(components, 'bootstrap')
    request.include(components, 'jquery')
    query = request.POST.get('query')
    query_tuple = re.split('; |, |\*|\n|\)|\(| |\.|،|:|؟|\?|,|\u200c', query.replace('\xa0', ' '))

    for word in query_tuple:

        if word in reverse_index:
            for page in reverse_index[word]:
                results[page] = results.get(page, 0) + 1

    results = sorted(results.items(), key=lambda x:x[1])[::-1]
    # print(results)


    return {'results': results, 'page_index': modified_page_index, 'query': query}
