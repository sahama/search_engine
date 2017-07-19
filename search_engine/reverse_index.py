import csv
import search_engine
import os
import re
from math import log

def create():
    url = 1
    content = 0

    reverse_index = {}
    page_index = []
    with open(os.path.join(search_engine.pkg_location, 'items1.csv'), newline='') as crawled_file:
        crawled = csv.reader(crawled_file)
        for page in crawled:
            if not page[url] in page_index:
                page_index.append(page[url])
            index = page_index.index(page[url])

            # for word in page[0].split():
            for word in re.split('; |, |\*|\n|\)|\(| |\.|،|:|؟|\?|,|\u200c|\"|',page[content].replace('\xa0', ' ')):
                if word:
                    if word in reverse_index:
                        reverse_index[word]['tf'][index] = reverse_index[word]['tf'].get(index, 0) + 1
                    else:
                        reverse_index[word] = {'tf':{index:1}}
                        # reverse_index[word] = {index:{'tf':1}}
                        # reverse_index[word].add(index)

    # print(reverse_index)
    page_count = len(page_index)

    for key in reverse_index:
        # print(key, page_count, len(reverse_index[key]['tf']) , 'idf', idf)
        idf = log(page_count/len(reverse_index[key]['tf']))
        reverse_index[key]['idf'] = idf

    # print(reverse_index)

    # tmp = {}
    # for i,j in enumerate(reverse_index):
    #     if i < 10:
    #         tmp[j] = reverse_index[j]
    # print(tmp)
    return reverse_index , page_index