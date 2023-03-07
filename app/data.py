# To create tables and insert initial records

import conn

# Create cursor for connection object
mycursor = conn.myconn.cursor()

# Use globehopperapp schema
mycursor.execute(
    "USE globehopperapp"
)

# Create Country & City tables
mycursor.execute(
    "DROP TABLE IF EXISTS Country"
)

mycursor.execute(
    "CREATE TABLE Country (" +
        "CountryId INT AUTO_INCREMENT  PRIMARY KEY," +
        "Name VARCHAR(100) NOT NULL," +
        "Population DOUBLE NOT NULL," +
        "Continent VARCHAR(250) NOT NULL)"
)

mycursor.execute(
    "DROP TABLE IF EXISTS City"
)

mycursor.execute(
    "CREATE TABLE City ("
    +"CityId INT AUTO_INCREMENT  PRIMARY KEY," + 
    "Name VARCHAR(100) NOT NULL," +
    "CountryId INT NOT NULL," +
    "Capital INT NOT NULL," +
    "FirstLandmark VARCHAR(250) NOT NULL," +
    "SecondLandmark VARCHAR(250) NOT NULL," +
    "ThirdLandmark VARCHAR(250) NOT NULL)"
)

# Insert initial records into tables
mycursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (1, 'Canada', 30000000, 'North America')")
mycursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (2, 'USA', 330000000, 'North America')")
mycursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (3, 'France', 3000000, 'Europe')")
mycursor.execute("INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (4, 'India', 300000000, 'Asia')")

mycursor.execute("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (1, 'Ottawa', 1, 1, 'Parliament House', 'Museum', 'Rideau Canal')")
mycursor.execute("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (2, 'Toronto', 1, 0, 'CN Tower', 'Niagara Falls', 'AGO')")
mycursor.execute("INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (3, 'Washington', 2, 1, 'White House', 'Lincoln Memorial', 'National Air and Space Museum')")

# Commit all SQL queries to connection
conn.myconn.commit()