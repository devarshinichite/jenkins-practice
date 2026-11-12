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
        'name': 'joe biden',
        'log': 'soddddaaaa',
        'status': 200 
    },
    {
        'name': 'doland trump',
        'log': 'obamnaa',
        'status': 200 
    })

@app.route('/about')
def apiKey():
    return jsonify({
        'name': 'Devarshi Nichite',
        'working': 'Jenkins Multipipeline Branch',
        'status': 'online',
        'branch': 'feature/test',
        'origin': 'main'
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
