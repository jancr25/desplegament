from flask import Flask, request
import os
import time
import logging

app = Flask(__name__)

@app.route('/')
def hello_instance():
    app.logger.info('Processing request for instance %s', app.instance_name)
    time.sleep(2)
    return "Hello from " + app.instance_name

app.instance_name = os.getenv('INSTANCE') if os.getenv('INSTANCE') else "No instance provided"
port = os.getenv('PORT') if os.getenv('PORT') else 5000
logfile = os.getenv('LOGFILE') if os.getenv('LOGFILE') else 'app.log'

logging.basicConfig(filename=logfile, level=logging.INFO)

if __name__ == '__main__':
    app.run(debug=True, port=port, host='0.0.0.0')
