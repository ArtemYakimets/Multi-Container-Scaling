import os
import random
import requests
import time

SIZE = int(os.getenv("SIZE"))
PRODUCER_ID = int(os.getenv("PRODUCER_ID"))
REQUEST_ATTEMPTS = int(os.getenv("REQUEST_ATTEMPTS"))
SEND_URL = os.getenv("SEND_URL")
FINISH_URL = os.getenv("FINISH_URL")

def send():
    num_elements = SIZE * SIZE
    for i in range(num_elements):
        element = random.randint(1, 1000)
        data = {"PRODUCER_ID": PRODUCER_ID, "index": i, "element": element}
        data_send_flag = 0

        for _ in range(REQUEST_ATTEMPTS):
            try:
                response = requests.post(SEND_URL, json=data)
                response.raise_for_status()
                data_send_flag = 1
                break
            except requests.exceptions.RequestException:
                time.sleep(1)
        if data_send_flag == 0:
            print(f"Error: Failed to send element (index:{i}, value:{element})")
        else:
            print(f"The element (index:{i}, value:{element}) is sent succesfully")


def finish():
    data = {"PRODUCER_ID": PRODUCER_ID, "SIZE": SIZE}
    data_send_flag = 0

    for _ in range(REQUEST_ATTEMPTS):
        try:
            response = requests.post(SEND_URL, json=data)
            response.raise_for_status()
            data_send_flag = 1
            break
        except requests.exceptions.RequestException:
            time.sleep(1)
    if data_send_flag == 0:
        print(f"Error: Failed to send the finish signal")
    else:
        print(f"The finish signal is sent succesfully")


if __name__ == '__main__':
    send()
    finish()
