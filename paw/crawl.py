# from stackapi import StackAPI
# import json
# import pprint
# SITE = StackAPI('stackoverflow')
# SITE.page_size = 10
# SITE.max_pages = 1
# tags = SITE.fetch('tags')

# print((tags["items"]))
# items = tags["items"]
# tags = {}
# print(items[0])
# print(type(items))
# print()
# a = tags.items

# print(a)

# for item in items:
import datetime
from stackapi import StackAPI
SITE = StackAPI('stackoverflow')
SITE.page_size = 100
SITE.max_pages = 10
tags = SITE.fetch('tags', min=20)
clist = tags["items"]
tags_list = []
for item in clist:
    tags_list.append(item["name"])
    now = datetime.datetime.now()
    print(item["name"]+","+"admin"+","+str(now))
