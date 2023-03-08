# Starting point of our WebApp - main
#    pip install Flask

from flask import Flask, request, jsonify
import country, city

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

@app.route('/countries/<continent>', methods=['GET'])
def get_countries_by_continent(continent):
    return country.get_countries_by_continent(continent)

# Read API - get all countries
@app.route('/countries', methods=['GET'])
def get_all_countries():
    return country.get_countries()

# Create API - add a city
@app.route('/cities', methods=['POST'])
def add_city():
    return city.add_city(request.json)

# Read API - get all cities
@app.route('/cities', methods=['GET'])
def get_all_cities():
    return city.get_all_cities()

# Execute on the terminal
if __name__ == '__main__':
    app.run()