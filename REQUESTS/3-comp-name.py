import json
import requests
from requests.exceptions import RequestException
import time

url = "https://jsonplaceholder.typicode.com/users"

start_time = time.perf_counter()

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    if response.status_code == 200:
        try:
            data = response.json()
            if isinstance(data, list):
                for user in data:
                    if user["id"] == 1:
                        company_name = user["company"]["name"]
                        print("company_name: ", company_name)
        except ValueError as exception:
            print("JSON decoding error: ", exception)
    else:
        print("response failed: ", response.status_code)
except RequestException as e:
    print("Networ error: ", e)
    data = None

if 'data' in locals():
    print("data type: ", type(data))

end_time = time.perf_counter()

response_time = end_time - start_time
print("response time: ", response_time)
