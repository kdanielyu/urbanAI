import os.path
import boto3

from flask import Flask, Response, send_file, redirect


app = Flask(__name__, static_url_path='/')

@app.route('/', methods=['GET'])
def index():
    return redirect("/index.html", code=302)

@app.route('/get-object', methods=['GET'])
def get_object_AWS():

    # add environ config file later
    s3 = boto3.resource(
        service_name='s3',
        region_name='ap-southeast-2',
        aws_access_key_id='key',
        aws_secret_access_key='secretkey'
    )

    s3.Bucket('urbanai').download(Filename='')

    return Response(status=404)

if __name__ == '__main__': 
    app.run(port=3000)
