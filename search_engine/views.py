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
    tmp_results = {}
    request.include(components, 'bootstrap')
    request.include(components, 'jquery')
    query = ''
    results = []
    if request.method == 'POST':
        query = request.POST.get('query')
        query_tuple = re.split('; |, |\*|\n|\)|\(| |\.|،|:|؟|\?|,|\u200c|\"', query.replace('\xa0', ' '))

        for word in query_tuple:

            if word in reverse_index:
                for page in reverse_index[word]['tf'].keys():
                    # results[page] = results.get(page, 0) + 1
                    tmp_results.setdefault(page, {})[word] = reverse_index[word]['idf']

        print(tmp_results)
        # results = sorted(tmp_results.items(), key=lambda x:sum([reverse_index[key]['idf'] for key in x[1]]))[::-1]
        results = sorted(tmp_results.items(), key=lambda x:sum([x[1][word] for word in x[1]]))[::-1]

    return {'results': results, 'page_index': modified_page_index, 'query': query}
