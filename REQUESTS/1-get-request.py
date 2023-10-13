import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    count = 0
    try:
        if isinstance(data, list):
            for post in data:
                if len(post["title"]) <= 20:
                    count += 1
                    print("the name : {}".format(post["title"]))
    except KeyError as e:
        print("error of {}".format(e))
    print("count : {}".format(count))
    print(type(data))

else:
    print("Request failed with statuse code ", response.status_code)

