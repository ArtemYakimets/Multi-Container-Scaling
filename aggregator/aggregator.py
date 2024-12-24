import numpy as np 
import requests
import time
import threading
from flask import Flask, request

app = Flask(__name__)

CONSUMER_URLS = [
    "http://app-consumer-1:8000/data",
    "http://app-consumer-2:8000/data",
    "http://app-consumer-3:8000/data",
    "http://app-consumer-4:8000/data",
    "http://app-consumer-5:8000/data",
    "http://app-consumer-6:8000/data",
    "http://app-consumer-7:8000/data",
    "http://app-consumer-8:8000/data",
    "http://app-consumer-9:8000/data",
    "http://app-consumer-10:8000/data"
]

start_time = time.time()

data1_ready = 0
data2_ready = 0

data1_size = 0
data2_size = 0


def collect_data():
    for url in CONSUMER_URLS:
        all_data = request.get(url).json()

        data1 = all_data["data1"]
        data2 = all_data["data2"]

    return data1, data2


@app.route("/finish", methods=["POST"])
def get_finish():
    global data1_ready, data2_ready, data1_size, data2_size

    data = request.json
    PRODUCER_ID = data["PRODUCER_ID"]
    SIZE = data["SIZE"]

    if PRODUCER_ID == 1:
        data1_ready = 1
        data1_size = SIZE
    elif PRODUCER_ID == 2:
        data2_ready = 2
        data2_size = SIZE
    else:
        return f"Error: Invalid PRODUCER_ID: {PRODUCER_ID}", 400

    if data1_ready and data2_ready:
        threading.Thread(target = aggregate).start()


def aggregate():
    global start_time, data1_size, data2_size

    while True:
        data1_raw, data2_raw = collect_data()

        data1_raw.sort(key=lambda x: x[0])
        data1 = [value for _, value in data1]
        data2_raw.sort(key=lambda x: x[0])
        data2 = [value for _, value in data2]

        if len(data1) != data1_size or len(data2) != data2_size or len(data1) != len(data2):
            time.sleep(1)
            continue

        size = int(data1_size ** 0.5)
        matrix1 = np.array().reshape(size, size)
        matrix2 = np.array(p2_data).reshape(size, size)
        result = np.dot(matrix1, matrix2)

        end_time = time.time()

        print(f"Matrix1:\n{matrix1}")
        print(f"Matrix2:\n{matrix2}")
        print(f"Result:{result}")

        print(f"Time spent:{end_time - start_time} seconds")

        return


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)