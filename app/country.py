# Define all functions related to Country RESTful APIs

from flask import Flask, request, jsonify
import services

# Function to create a country
def create_country(data):
    services.create_country(data)
    return jsonify({
        "message": 'Data inserted successfully!'
    })

# Function to update a current country in Country table
def update_country(id, data):
    services.update_country(id, data)
    return jsonify({
        "message": 'Data successfully updated!'
    })

# Function to delete a country from the Country table
def delete_country(id):
    services.delete_country(id)
    return jsonify({
        'message': 'Data with Country ID = ' + str(id) + 'successfully deleted!'
    })

# Function to get countries by a continent
def get_countries_by_continent(continent):
    results = services.get_countries_by_continent(continent)

    data = []
    for row in results:
        data.append({
            "CountryId": row[0],
            "Name": row[1],
            "Population": row[2],
            "Continent": row[3]
        })

    return jsonify(data) 

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