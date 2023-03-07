# Define all functions related to Country RESTful APIs

from flask import Flask, request, jsonify
import services

# Function to get all countries and return as a JSON object  
def getCountries():
    results = services.allCountries()
    return jsonify(results)