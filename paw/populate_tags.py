import requests
import json


def main():
    li = open('tags.txt', 'r').readlines()
    for i in li:
        i = i.split(',')[0]
        # print(i)

        requests.post(url='http://127.0.0.1:8000/addTag', data={
            'name': i
        })


if __name__ == "__main__":
    main()
