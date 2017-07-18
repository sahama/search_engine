import csv
import search_engine
import os
import re
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
            for word in re.split('; |, |\*|\n|\)|\(| |\.|،|:|؟|\?|,|\u200c',page[content].replace('\xa0', ' ')):
                if word:
                    if word in reverse_index:
                        reverse_index[word].add(index)
                    else:
                        reverse_index[word] = set()
                        reverse_index[word].add(index)


    # tmp = {}
    # for i,j in enumerate(reverse_index):
    #     if i < 10:
    #         tmp[j] = reverse_index[j]
    # print(tmp)
    return reverse_index , page_index