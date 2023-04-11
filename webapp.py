from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/costOfEquity', methods=['GET'])
def myroute():
    # Convert GET arguments to a dictionary
    args_dict = {key: val for key, val in request.args.items()}

    # Check if necessary arguments are present
    if 'ticker' not in args_dict or 'premium' not in args_dict:
        return 'Error: ticker and premium arguments are required'

    # Call CLI app with necessary arguments
    cli_args = ["python",'/app/costOfEquity.py', args_dict['ticker'], args_dict['premium']]
    for key, val in args_dict.items():
        if val is not None and val != '' and key not in ['ticker', 'premium']:
            cli_args.append('--' + key)
            cli_args.append(val)

    # Call CLI app
    result = subprocess.check_output(cli_args)

    return jsonify({'results': result.decode('utf-8'),"requests":args_dict})
    # return 'Arguments processed successfully'

if __name__ == '__main__':
    app.run(port=8080)