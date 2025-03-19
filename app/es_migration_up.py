import os
import mysql.connector
from dotenv import load_dotenv
from es_client import (
    create_indexes,
    index_vehicle,
    index_part,
    index_media,
    index_media_ocrs,
    index_part_categories,
    index_part_groups,
    index_part_images,
    index_part_number_cars,
    index_part_image_ocrs,
    index_part_image_ocr_has_part_number_cars,
    index_part_has_vehicles,
    index_part_has_vehicle_has_variants,
    index_part_has_vehicle_has_model_years,
    index_part_has_vehicle_has_production_years,
    index_part_number_car_has_variants,
    index_vehicle_has_model_years,
    index_vehicle_has_production_years,
    index_vehicle_has_variants,
    index_vehicle_has_source_of_truths,
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
    print("creating index vehicles")

    for vehicle in vehicles:
        index_vehicle(vehicle['id'], vehicle)

def index_all_parts():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM parts")
    datas = cursor.fetchall()
    print("creating index parts")

    for val in datas:
        index_part(val['id'], val)

def index_all_part_categories():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_categories")
    datas = cursor.fetchall()
    print("creating index part_categories")

    for val in datas:
        index_part_categories(val['id'], val)

def index_all_part_groups():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_groups")
    datas = cursor.fetchall()
    print("creating index part_groups")

    for val in datas:
        index_part_groups(val['id'], val)

def index_all_part_images():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_images")
    datas = cursor.fetchall()
    print("creating index part_images")

    for val in datas:
        index_part_images(val['id'], val)

def index_all_part_number_cars():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_number_cars")
    datas = cursor.fetchall()
    print("creating index part_number_cars")

    for val in datas:
        index_part_number_cars(val['id'], val)

def index_all_part_image_ocrs():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_image_ocrs")
    datas = cursor.fetchall()
    print("creating index part_image_ocrs")

    for val in datas:
        index_part_image_ocrs(val['id'], val)

def index_all_part_image_ocr_has_part_number_cars():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_image_ocr_has_part_number_cars")
    datas = cursor.fetchall()
    print("creating index part_image_ocr_has_part_number_cars")

    for val in datas:
        index_part_image_ocr_has_part_number_cars(val['id'], val)

def index_all_part_has_vehicle_has_variants():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_has_vehicle_has_variants")
    datas = cursor.fetchall()
    print("creating index part_has_vehicle_has_variants")

    for val in datas:
        index_part_has_vehicle_has_variants(val['my_row_id'], val)

def index_all_part_has_vehicles():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_has_vehicles")
    datas = cursor.fetchall()
    print("creating index part_has_vehicles")

    for val in datas:
        index_part_has_vehicles(val['id'], val)

def index_all_part_has_vehicle_has_model_years():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_has_vehicle_has_model_years")
    datas = cursor.fetchall()
    print("creating index part_has_vehicle_has_model_years")

    for val in datas:
        index_part_has_vehicle_has_model_years(val['my_row_id'], val)

def index_all_part_has_vehicle_has_production_years():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_has_vehicle_has_production_years")
    datas = cursor.fetchall()
    print("creating index part_has_vehicle_has_production_years")

    for val in datas:
        index_part_has_vehicle_has_production_years(val['my_row_id'], val)

def index_all_part_number_car_has_variants():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM part_number_car_has_variants")
    datas = cursor.fetchall()
    print("creating index part_number_car_has_variants")

    for val in datas:
        index_part_number_car_has_variants(val['id'], val)

def index_all_vehicle_has_model_years():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicle_has_model_years")
    datas = cursor.fetchall()
    print("creating index vehicle_has_model_years")

    for val in datas:
        index_vehicle_has_model_years(val['id'], val)

def index_all_vehicle_has_production_years():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicle_has_production_years")
    datas = cursor.fetchall()
    print("creating index vehicle_has_production_years")

    for val in datas:
        index_vehicle_has_production_years(val['id'], val)

def index_all_vehicle_has_variants():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicle_has_variants")
    datas = cursor.fetchall()
    print("creating index vehicle_has_variants")

    for val in datas:
        index_vehicle_has_variants(val['id'], val)

def index_all_vehicle_has_source_of_truths():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicle_has_source_of_truths")
    datas = cursor.fetchall()
    print("creating index vehicle_has_source_of_truths")

    for val in datas:
        index_vehicle_has_source_of_truths(val['id'], val)


def index_all_medias():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM media")
    datas = cursor.fetchall()
    print("creating index media")

    for val in datas:
        index_media(val['id'], val)

def index_all_media_ocrs():
    cursor = mysql_conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM media_ocrs")
    datas = cursor.fetchall()
    print("creating index media_ocrs")

    for val in datas:
        index_media_ocrs(val['id'], val)

# Call these functions to index all entities
#create entities
create_indexes()
#create seeder
index_all_vehicles()
index_all_vehicle_has_model_years()
index_all_vehicle_has_production_years()
index_all_vehicle_has_variants()
index_all_vehicle_has_source_of_truths()
index_all_parts()
index_all_medias()
index_all_media_ocrs()
index_all_part_groups()
index_all_part_number_cars()
index_all_part_images()
index_all_part_image_ocrs()
index_all_part_categories()
index_all_part_has_vehicles()
index_all_part_has_vehicle_has_model_years()
index_all_part_has_vehicle_has_production_years()
index_all_part_number_car_has_variants()
index_all_part_has_vehicle_has_variants()

