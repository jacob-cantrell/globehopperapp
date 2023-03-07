# Define all services for Country & City

from flask import Flask, request, jsonify
import conn

# Gets all records from Country table using SQL
def allCountries():
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