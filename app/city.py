# Define all functions related to City RESTful APIs

from flask import Flask, request, jsonify
import services

# Function to create a city
def add_city(data):
    services.create_city(data)
    return jsonify({
        "message": 'Data inserted successfully!'
    })

# Function to get all cities
def get_all_cities():
    results = services.all_cities()

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