import csv
import mysql.connector
from key import db_pwd

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password= db_pwd,
    database="transactionaldata"
)

# Create cursor object to execute commands to the database
cursor = connection.cursor()

# Define the column names and data types for the table
columns = [
    ("transaction_id", "INT"),
    ("merchant_id", "INT"),
    ("user_id", "INT"),
    ("card_number", "VARCHAR(255)"),
    ("transaction_date", "DATETIME"),
    ("transaction_amount", "DECIMAL(10,2)"),
    ("device_id", "VARCHAR(255)"),
    ("has_cbk", "TINYINT(1)")
]

# Generate the CREATE TABLE query
table_name = "transactional_sample"
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
create_table_query += ", ".join([f"{column_name} {column_type}" for column_name, column_type in columns])
create_table_query += ")"

# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Upload transactional-sample.csv into the database
with open('transactional-sample.csv', 'r') as file:
    csv_data = csv.DictReader(file)

    for row in csv_data:
        # Extract the values from the row
        values = [
            int(row["transaction_id"]),
            int(row["merchant_id"]),
            int(row["user_id"]),
            row["card_number"],
            row["transaction_date"],
            float(row["transaction_amount"]),
            row["device_id"],
            row["has_cbk"].upper() == "TRUE"  # Convert "TRUE" to True and "FALSE" to False
        ]

        # Insert the data into the database using explicit syntax
        query = f"INSERT INTO {table_name} (transaction_id, merchant_id, user_id, card_number, transaction_date, transaction_amount, device_id, has_cbk) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, values)

connection.commit()
connection.close()
