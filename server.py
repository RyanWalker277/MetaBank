from email.mime import base
from urllib import response
from flask import Flask , request , jsonify
import requests

app = Flask(__name__)

@app.route('/')
def bot():
    if request.method == "GET":
        base_url = 'http://api.wolframalpha.com/v1/spoken?appid=9YVPQP-9249U8W794&i=' 
        ques = request.args['question']
        final = ques.replace(" ", "+")
        url = base_url + final
        response = requests.get(url)
        return response.text
        
if __name__ == '__main__':
    app.run(debug=True)

