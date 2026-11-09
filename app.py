from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome Hello world!',
        'status': 'success',
        'health check': 'OK',
    })

@app.route('/api/data')
def apiKey():
    return jsonify({
        'name': 'Devarshi Nichite',
        'log': 'Working on Jenkins pipeline',
        'status': 200 
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
