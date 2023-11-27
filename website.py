import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

API_KEY = "i47r4fw47h4wfi7wofbwo74gwrgo3pd38dhdq"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exit', methods=['POST'])
def exit_program():
    api_key = request.form.get('api_key')
    action = request.form.get('action')

    if api_key == API_KEY and action == 'exit':
        response = jsonify({'message': 'Program will be exited.'})
        os._exit(0)
    else:
        response = jsonify({'message': 'Invalid API key or action.'})

    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(host='194.61.52.232', port=8081, debug=True)
