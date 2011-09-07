from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def default():
    """Default route"""
    return send_static_file('default.html')


@app.route('/image/<url>', methods=['GET',])
def procImg(url):
    """GET /image/<url>

    Process image at url and returns stat."""
    return jsonify(image=url)

if __name__ == '__main__':
    app.debug = False 
    app.run(host='0.0.0.0')
