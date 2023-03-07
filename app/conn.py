# Connect to MySQL database

import mysql.connector;

myconn = mysql.connector.connect(
    host="localhost",
    user="ally",
    password="ally123$",
    database="globehopperapp"
)