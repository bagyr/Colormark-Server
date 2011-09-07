from flask import Flask, jsonify, abort
from procImg import process

app = Flask(__name__)

@app.route("/")
def default():
    """Default route"""
    abort(403)


@app.route('/image/<url>', methods=['GET',])
def procImg(url):
    """GET /image/<url>

    Process image at url and returns stat."""
    res = process(url)
    return jsonify(result = res['result'], size = res['size'], format = res['format'])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
