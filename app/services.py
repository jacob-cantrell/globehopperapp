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

# Gets City record where City is capital of specified Country
def get_capital_from_country(country_name):
    # Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    # Get values & query
    query = "SELECT CityId, City.Name, City.CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark FROM City LEFT JOIN Country ON City.CountryId = Country.CountryId WHERE Capital=1 AND Country.Name=%s"

    # Execute SQL Query
    mycursor.execute(
        query,
        [country_name]
    )
    results = mycursor.fetchall()

    # Close connection
    mycursor.close()
    conn.myconn.close()

    return results

# Gets all Country records where Continent = continent param
def get_countries_by_continent(continent):
    # Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    # Execute SQL Query
    mycursor.execute(
        "SELECT * FROM Country WHERE Continent=%s",
        [continent]
    )
    results = mycursor.fetchall()

    # Close connection
    mycursor.close()
    conn.myconn.close()

    return results

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

# Adds a new City record to City table
def create_city(data):
    # Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    # Get values & query
    query = "INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (
        data['CityId'],
        data['Name'],
        data['CountryId'],
        data['Capital'],
        data['FirstLandmark'],
        data['SecondLandmark'],
        data['ThirdLandmark']
    )

    # Execute SQL Query
    mycursor.execute(
        query,
        values
    )

    # Close connection
    mycursor.close()
    conn.myconn.close()

# Updates a current City
def update_city(id, data):
    # Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    # Get query & values
    query = "UPDATE City SET Name=%s, CountryId=%s, Capital=%s, FirstLandmark=%s, SecondLandmark=%s, ThirdLandmark=%s WHERE CityId=%s"
    values = (
        data['Name'],
        data['CountryId'],
        data['Capital'],
        data['FirstLandmark'],
        data['SecondLandmark'],
        data['ThirdLandmark'],
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

# Deletes current City record based on CityId
def delete_city(city_id):
    # Open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    # Execute SQL Query
    mycursor.execute(
        "DELETE FROM City WHERE CityId=" + str(city_id)
    )

    # Close connection
    mycursor.close()
    conn.myconn.close()


# Gets all records from City
def all_cities():
    # Open Connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    # Execute SQL Query
    mycursor.execute(
        "SELECT * FROM City"
    )
    results = mycursor.fetchall()

    # Close connection
    mycursor.close()
    conn.myconn.close()

    return results