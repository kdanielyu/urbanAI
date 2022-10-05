import os.path

from flask import Flask, Response, send_file


app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def index():
    return Response(status=404)

@app.route('/get-object', methods=['GET'])
def get_object_AWS():
    return Response(status=404)

if __name__ == '__main__': 
    app.run(port=3000)
