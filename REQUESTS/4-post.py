import requests
from requests.exceptions import RequestException, HTTPError
import time

url = "https://jsonplaceholder.typicode.com/posts"

payload = {"title": "call me", "body": "This is the body"}

start_time = time.perf_counter()
try:
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    if response.status_code == 201:
        try:
            data = response.json()
            if isinstance(data, dict):
                print("response data: ",data)
                print("data type: ", type(data))
            else:
                print("data not a method")
        except ValueError as err:
            print("json decoding error: ", err)
    else:
        print("request returned with: ", response.status_code)
except HTTPError as httperror:
    print("http error with: ", httperror)
except RequestException as exception:
    print("request exception: ", exception)

if 'data' in locals():
    print(type(data))
end_time = time.perf_counter()

response_time = end_time - start_time
print("response time: ", response_time)
