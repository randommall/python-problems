import requests
import json
import time

url = "https://jsonplaceholder.typicode.com/posts"

start_time = time.perf_counter()
try:

    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Network error", e)
    data = None

else:
    if response.status_code == 200:
        try:
            data = response.json()
        except json.JSONDecodeError as exception:
            print("JSON decoding error: ",exception)

    else:
        print("rewust failed with: ", response.status_code)
        data = None

end_time = time.perf_counter()

if 'data' in locals():
    print("data type: ", type(data))


response_time = end_time - start_time
print("response time: {}".format(response_time))
