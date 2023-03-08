# Starting point of our WebApp - main
#    pip install Flask

from flask import Flask, request, jsonify
import country

# Using Flask framework
app = Flask(__name__)

# Create API
@app.route('/countries', methods=['POST'])
def create_country():
    data = request.json
    return country.create_country(data)

# Update Country API
@app.route('/countries/<int:id>', methods=['PUT'])
def update_country(id):
    return country.update_country(id, request.json)

# Delete Country API
@app.route('/countries/<int:id>', methods=['DELETE'])
def delete_country(id):
    return country.delete_country(id)

# Read API - get all countries
@app.route('/countries', methods=['GET'])
def get_all_countries():
    return country.get_countries()

# Execute on the terminal
if __name__ == '__main__':
    app.run()