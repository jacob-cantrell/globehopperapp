# Define all services for Country & City

from flask import Flask, request, jsonify
import conn

# Adds a new Country record to the Country table
def create_country(data):
    # Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    # Get data
    values = (
        data['CountryId'], 
        data['Name'], 
        data['Population'], 
        data['Continent']
    )
    query = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)" 

    # Execute SQL Query
    mycursor.execute(
        query,
        values
    )

    # Close connection
    mycursor.close()
    conn.myconn.close()

# Updates current record in Country table
def update_country(id, data):
    # Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    # Get values
    query = "UPDATE Country SET Name=%s, Population=%s, Continent=%s WHERE CountryId=%s"
    values = (
        data['Name'],
        data['Population'],
        data['Continent'],
        id
    )

    # Execute SQL Query
    mycursor.execute(
        query,
        values
    )

    # Close connection
    mycursor.close()
    conn.myconn.close()

# Deletes record from Country table based on id
def delete_country(id):
    # Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    # Execute SQL Query
    mycursor.execute(
        "DELETE FROM Country WHERE CountryId=" + str(id)
    )

    # Close connection
    mycursor.close()
    conn.myconn.close()

# Gets all records from Country table using SQL
def all_countries():
    # Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor() 

    # Execute SQL query
    mycursor.execute("SELECT * FROM Country")
    results = mycursor.fetchall()

    # Close connection
    mycursor.close()
    conn.myconn.close()

    return results