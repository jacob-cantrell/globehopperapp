# Define all functions related to Country RESTful APIs

from flask import Flask, request, jsonify
import services

# Function to create a country
def create_country(data):
    services.create_country(data)
    return jsonify({
        "message": 'Data inserted successfully'
    })

# Function to get all countries and return as a JSON object  
def get_countries():
    results = services.all_countries()

    data = []
    for row in results:
        data.append({
            "CountryId": row[0],
            "Name": row[1],
            "Population": row[2],
            "Continent": row[3]
        })

    return jsonify(data)