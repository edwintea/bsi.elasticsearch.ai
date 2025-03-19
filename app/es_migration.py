import os
import mysql.connector
from dotenv import load_dotenv
from es_client import (
    index_vehicle,
    index_part,
    index_media,
    index_part_categories,
    index_part_groups,
    index_part_has_vehicle_has_model_years,
    index_part_has_vehicle_has_production_years
    )

# Load environment variables from .env file
load_dotenv()

# MySQL connection setup using environment variables
mysql_conn = mysql.connector.connect(
    host=os.getenv("DB_SERVER_LOCAL"),
    user=os.getenv("DB_USER_LOCAL"),
    password=os.getenv("DB_PASSWORD_LOCAL"),
    database=os.getenv("DB_NAME_LOCAL")
)

def index_all_vehicles():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicles")
    vehicles = cursor.fetchall()

    for vehicle in vehicles:
        index_vehicle(vehicle['id'], vehicle)

def index_all_parts():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM parts")
    parts = cursor.fetchall()

    for part in parts:
        index_part(part['id'], part)

def index_all_part_categories():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_categories")
    parts = cursor.fetchall()
    print("index_all_part_categories")

    for part in parts:
        index_part_categories(part['id'], part)

def index_all_part_groups():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_groups")
    parts = cursor.fetchall()

    for part in parts:
        index_part_groups(part['id'], part)

def index_all_part_has_vehicle_has_model_years():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_has_vehicle_has_model_years")
    parts = cursor.fetchall()

    for part in parts:
        index_part_has_vehicle_has_model_years(part['id'], part)

def index_all_part_has_vehicle_has_production_years():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_has_vehicle_has_production_years")
    parts = cursor.fetchall()

    for part in parts:
        index_part_has_vehicle_has_production_years(part['id'], part)

def index_all_medias():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM media")
    medias = cursor.fetchall()

    for media in medias:
        index_media(media['id'], media)

# Call these functions to index all vehicles and parts
index_all_vehicles()
index_all_parts()
index_all_medias()
index_all_part_groups()
index_all_part_categories()
index_all_part_has_vehicle_has_model_years()
index_all_part_has_vehicle_has_production_years()