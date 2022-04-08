from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    ip_addr = request.environ['REMOTE_ADDR']
    return '<h1> This is docker ip- ' + ip_addr
app.run(host="0.0.0.0", port=80)