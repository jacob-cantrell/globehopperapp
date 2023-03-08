# Define all functions related to City RESTful APIs

from flask import Flask, request, jsonify
import services

# Function to create a city
def add_city_view(data):
    services.create_city_service(data)
    return jsonify({
        "message": 'Data inserted successfully!'
    })

# Function to update a city
def update_city_view(city_id, data):
    services.update_city_service(city_id, data)
    return jsonify({
        'message': 'Data with CityId = ' + str(city_id) + ' updated successfully!'
    })

def delete_city_view(city_id):
    services.delete_city_service(city_id)
    return jsonify({
        'message': 'Data with CityId = ' + str(city_id) + ' was successfully deleted!'
    })

# Function to get all cities
def get_all_cities_view():
    results = services.all_cities_service()

    data = []
    for row in results:
        data.append({
            "CityId": row[0],
            "Name": row[1],
            "CountryId": row[2],
            "Capital": row[3],
            "FirstLandmark": row[4],
            "SecondLandmark": row[5],
            "ThirdLandmark": row[6]
        })

    return jsonify(data)