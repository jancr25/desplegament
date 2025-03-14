from flask import Flask, request 
import argparse 
import logging 

app = Flask(__name__) 

@app.route('/') 
def hello_instance(): 
    app.logger.info('Processing request for instance %s', app.instance_name) 
    return "Hello from " + app.instance_name 
  
if __name__ == '__main__': 
    parser = argparse.ArgumentParser() 
    parser.add_argument("-instance", help="Nom de la instància") 
    parser.add_argument("-port", type=int, help="Port on which to run the server") 
    parser.add_argument("-logfile", help="Log file") 
    args = parser.parse_args()
  
    app.instance_name = args.instance if args.instance else "No instance provided" 
    port = args.port if args.port else 5000 
    logfile = args.logfile if args.logfile else 'app.log' 
  
    logging.basicConfig(filename=logfile, level=logging.INFO) 
  
    app.run(debug=True, port=port) 
