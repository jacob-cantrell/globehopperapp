# Starting point of our WebApp - main
#    pip install Flask

from flask import Flask, request, jsonify
import country

# Using Flask framework
app = Flask(__name__)

# Read API - get all countries
@app.route('/countries', methods=['GET'])
def get_all_countries():
    return country.get_countries()

# Execute on the terminal
if __name__ == '__main__':
    app.run()