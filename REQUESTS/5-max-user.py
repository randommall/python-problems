import requests
from requests.exceptions import RequestException, HTTPError
import time


url = "https://jsonplaceholder.typicode.com/users"

start_time = time.perf_counter()

try:
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    if response.status_code == 200:
        try:
            data = response.json()
            with open("data.json", "w") as f:
                json.dump(data, f)

            id_list = []
            for user in data:
                user_id = user["id"]
                id_list.append(user_id)
            max_id = max(id_list)
            print("max user_id: ", max_id)
        except ValueError as err:
            print("response not a json format: ", err)
    else:
        print("response returned status code: ", response.status_code)
except RequestException as exc:
    print("request failed wit: ", exc)
    data = None

end_time = time.perf_counter()

if 'data' in locals():
    print("Data type is: ", type(data))

response_time = end_time - start_time

print("performance time ", response_time)
