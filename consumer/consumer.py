from flask import Flask, request, jsonify

app = Flask(__name__)

data1 = []
data2 = []


@app.route('/send', methods=['POST'])
def update_data():
    global data1, data2

    data = request.json
    
    PRODUCER_ID = data["PRODUCER_ID"]
    index = data["index"]
    element = data["element"]

    if PRODUCER_ID == 1:
        data1.append((index, element))
    elif PRODUCER_ID == 2:
        data2.append((index, element))
    else:
        return f"Error: Invalid PRODUCER_ID: {PRODUCER_ID}", 400

    return '', 200


@app.route('/data', methods=["GET"])
def return_data():
    return jsonify({"data1": data1, "data2": data2})


@app.get("/healthcheck")
def healthcheck():
    return {"status": "OK"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)