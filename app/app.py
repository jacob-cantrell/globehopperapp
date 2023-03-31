# Starting point of our WebApp - main
#    pip install Flask

from flask import Flask, request, jsonify
import country, city

# Using Flask framework
app = Flask(__name__)

# Create API
@app.route('/countries', methods=['POST'])
def create_country():
    return country.create_country_view(request.json)

# Update Country API
@app.route('/countries/<int:country_id>', methods=['PUT'])
def update_country(country_id):
    return country.update_country_view(country_id, request.json)

# Delete Country API
@app.route('/countries/<int:country_id>', methods=['DELETE'])
def delete_country(country_id):
    return country.delete_country_view(country_id)

# GET Countries by continent
@app.route('/countries/<continent>', methods=['GET'])
def get_countries_by_continent(continent):
    return country.get_countries_by_continent_view(continent)

# Read API - get City record from Capital City of Country specified
@app.route('/countries/<country_name>/1', methods=['GET'])
def get_capital_from_country(country_name):
    return country.get_capital_from_country_view(country_name)

# Read API - get all countries
@app.route('/countries', methods=['GET'])
def get_all_countries():
    return country.get_countries_view()

# Create API - add a city
@app.route('/cities', methods=['POST'])
def add_city():
    return city.add_city_view(request.json)

# Update API - update (put) a current city record
@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    return city.update_city_view(city_id, request.json)

# Delete API - delete a current City record
@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    return city.delete_city_view(city_id)

# Read API - get all cities
@app.route('/cities', methods=['GET'])
def get_all_cities():
    return city.get_all_cities_view()

# Execute on the terminal
if __name__ == '__main__':
    app.run()