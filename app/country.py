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
def update_country(country_id, data):
    services.update_country(country_id, data)
    return jsonify({
        "message": 'Data with CountryId = ' + str(country_id) + ' successfully updated!'
    })

# Function to delete a country from the Country table
def delete_country(country_id):
    services.delete_country(country_id)
    return jsonify({
        'message': 'Data with Country ID = ' + str(country_id) + ' successfully deleted!'
    })

# Function to get City record where City is capital of country
def get_capital_from_country(country_name):
    results = services.get_capital_from_country(country_name)

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