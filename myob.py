from flask import Flask,jsonify,request
import requests


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/health')
def health():
    r = requests.get(request.url)
    if r.status_code==200:
        return jsonify(message="Service Operating Normally",Status=r.status_code)
    else:
        return jsonify(message="Service Down", Status=r.status_code)

@app.route('/metadata')
def metadata():
    repo = 'maheshmarri/flaskapp_myob'
    r = requests.get('https://api.github.com/repos/{0}/commits?per_page=1'.format(repo))
    commit = r.json()[0]["sha"]
    json = {
        "myapplication": [
            {
                "version": "1.0",
                "description": "pre-interview technical test",
                "lastcommitsha": commit
            }
        ]
    }
    return jsonify(json)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)

