import datetime
from stackapi import StackAPI
SITE = StackAPI('stackoverflow')
SITE.page_size = 100
SITE.max_pages = 10000
tags = SITE.fetch('tags', min=20)
clist = tags["items"]
fp = open('tags.txt', "w")
for item in clist:
    print(item["name"])
    fp.write(item['name'])
