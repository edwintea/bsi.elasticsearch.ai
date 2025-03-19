import os

from elasticsearch import Elasticsearch
from fastapi.responses import JSONResponse
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# Initialize the Elasticsearch client
es = Elasticsearch(os.getenv("ELASTICSEARCH_LOCAL"))


def create_indexes():
    """Create Elasticsearch indexes for vehicles and parts."""
    # Create vehicles index
    vehicles_mapping = {
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "slug": {"type": "keyword"},
                "description": {"type": "text"},
                "image": {"type": "long"},  # Assuming image is a reference ID
                "model": {"type": "text"},
                "status": {"type": "integer"},
                "meta": {"type": "text"},
                "created_at": {"type": "date"},
                "updated_at": {"type": "date"},
                "deleted_at": {"type": "date"},
                "published_at": {"type": "date"},
                "category_description": {"type": "text"},
                "emission": {"type": "text"},
                "suggest": {
                    "type": "completion"  # Add this field for suggestions
                },
            }
        }
    }
    es.indices.create(index="vehicles", body=vehicles_mapping, ignore=400)

    # Create parts index
    parts_mapping = {
        "mappings": {
            "properties": {
                "code": {"type": "keyword"},
                "name": {"type": "text"},
                "part_group_id": {"type": "long"},
                "part_category_id": {"type": "long"},
                "image": {"type": "long"},  # Assuming image is a reference ID
                "description": {"type": "text"},
                "status": {"type": "integer"},
                "meta": {"type": "text"},
                "published_at": {"type": "date"},
                "created_at": {"type": "date"},
                "updated_at": {"type": "date"},
                "deleted_at": {"type": "date"},
                "suggest": {
                    "type": "completion"  # Add this field for suggestions
                },
            }
        }
    }
    es.indices.create(index="parts", body=parts_mapping, ignore=400)

    # Create media index
    media_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "long"},  # Primary key
                "model_type": {"type": "keyword"},  # Type of model (e.g., vehicle, part)
                "model_id": {"type": "long"},  # ID of the related model
                "uuid": {"type": "keyword"},  # Unique identifier
                "collection_name": {"type": "keyword"},  # Name of the collection
                "name": {"type": "text"},  # Name of the media file
                "file_name": {"type": "text"},  # Actual file name
                "mime_type": {"type": "keyword"},  # MIME type of the file
                "disk": {"type": "keyword"},  # Storage disk
                "conversions_disk": {"type": "keyword"},  # Disk for conversions
                "size": {"type": "long"},  # Size of the file
                "manipulations": {"type": "text"},  # Manipulations applied to the media
                "custom_properties": {"type": "text"},  # Custom properties
                "generated_conversions": {"type": "text"},  # Generated conversions
                "responsive_images": {"type": "text"},  # Responsive images
                "order_column": {"type": "integer"},  # Order column for sorting
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
                "suggest": {
                    "type": "completion"  # Add this field for suggestions
                },
            }
        }
    }

    # Create the media index in Elasticsearch
    es.indices.create(index="media", body=media_mapping, ignore=400)

    # Create media_ocrs index
    media_ocrs_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "long"},  # Primary key
                "created_at": {"type": "date"},  # Timestamp for creation
                "updated_at": {"type": "date"},  # Timestamp for last update
                "media_id": {"type": "long"},  # Reference to media
                "name": {"type": "text"},  # Name of the media OCR
                "ocr_raw": {"type": "text"},  # Raw OCR text
                "ocr_applied": {"type": "text"},  # Processed OCR text
                "ocr_applied_hash": {"type": "keyword"},  # Hash of the applied OCR
                "percentage": {"type": "integer"},  # Percentage value
                "folder_id": {"type": "long"},  # Reference to folder
                "folder_path": {"type": "text"},  # Path to the folder
                "status": {"type": "integer"},  # Status of the OCR
                "meta": {"type": "text"},  # Additional metadata
            }
        }
    }
    response = es.indices.create(index="media_ocrs",
                                 body=media_ocrs_mapping, ignore=400)
    if 'error' in response:
        print(f"Error creating index media ocrs: {response['error']}")

    # Create the part_categories index in Elasticsearch
    part_categories_mapping = {
        "mappings": {
            "properties": {
                "name": {"type": "text"},
                "image": {"type": "long"},  # Assuming image is a reference ID
                "description": {"type": "text"},
                "x": {"type": "double"},
                "y": {"type": "double"},
                "status": {"type": "integer"},
                "meta": {"type": "text"},
                "created_at": {"type": "date"},
                "updated_at": {"type": "date"},
                "deleted_at": {"type": "date"},
                "suggest": {
                    "type": "completion"  # Add this field for suggestions
                },
            }
        }
    }
    response=es.indices.create(index="part_categories", body=part_categories_mapping, ignore=400)
    if 'error' in response:
        print(f"Error creating index media ocrs: {response['error']}")

    #create index part_groups in elastic
    part_groups_mapping = {
        "mappings": {
            "properties": {
                "code": {"type": "keyword"},  # Unique code for the part group
                "name": {"type": "text"},
                "part_category_id": {"type": "long"},  # Reference to part category
                "image": {"type": "long"},  # Assuming image is a reference ID
                "description": {"type": "text"},
                "status": {"type": "integer"},
                "meta": {"type": "text"},
                "created_at": {"type": "date"},
                "updated_at": {"type": "date"},
                "deleted_at": {"type": "date"},
                "suggest": {
                    "type": "completion"  # Add this field for suggestions
                },
            }
        }
    }
    response=es.indices.create(index="part_groups", body=part_groups_mapping, ignore=400)
    if 'error' in response:
        print(f"Error creating index part_groups: {response['error']}")

    part_has_vehicle_has_model_years_mapping = {
        "mappings": {
            "properties": {
                "my_row_id": {"type": "long"},  # Reference to part_has_vehicle
                "part_has_vehicle_id": {"type": "long"},  # Reference to part_has_vehicle
                "value": {"type": "text"},  # The value associated with the model year
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
            }
        }
    }
    es.indices.create(index="part_has_vehicle_has_model_years", body=part_has_vehicle_has_model_years_mapping, ignore=400)

    part_has_vehicle_has_production_years_mapping = {
        "mappings": {
            "properties": {
                "my_row_id ": {"type": "long"},  # Reference to part_has_vehicle
                "part_has_vehicle_id": {"type": "long"},  # Reference to part_has_vehicle
                "value": {"type": "text"},  # The value associated with the production year
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
            }
        }
    }
    es.indices.create(index="part_has_vehicle_has_production_years", body=part_has_vehicle_has_production_years_mapping, ignore=400)

    part_has_vehicle_has_variants_mapping = {
        "mappings": {
            "properties": {
                "my_row_id ": {"type": "long"},  # Reference to part_has_vehicle
                "part_has_vehicle_id": {"type": "long"},  # Reference to part_has_vehicle
                "value": {"type": "text"},  # The value associated with the variant
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
            }
        }
    }
    es.indices.create(index="part_has_vehicle_has_variants", body=part_has_vehicle_has_variants_mapping, ignore=400)

    part_has_vehicles_mapping = {
        "mappings": {
            "properties": {
                "vehicle_id": {"type": "long"},  # Reference to vehicle
                "part_id": {"type": "long"},  # Reference to part
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
            }
        }
    }
    es.indices.create(index="part_has_vehicles", body=part_has_vehicles_mapping, ignore=400)

    part_image_ocr_has_part_number_cars_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "keyword"},  # Unique identifier
                "part_image_ocr_id": {"type": "keyword"},  # Reference to part image OCR
                "code": {"type": "text"},  # Code associated with the part number
                "part_number": {"type": "text"},  # The part number
                "vehicle_id": {"type": "long"},  # Reference to vehicle
                "part_id": {"type": "long"},  # Reference to part
                "part_image_id": {"type": "long"},  # Reference to part image
                "part_number_car_id": {"type": "long"},  # Reference to part number car
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
            }
        }
    }
    es.indices.create(index="part_image_ocr_has_part_number_cars", body=part_image_ocr_has_part_number_cars_mapping, ignore=400)

    part_image_ocrs_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "keyword"},  # Unique identifier
                "code": {"type": "text"},  # Code associated with the OCR
                "text_ori": {"type": "text"},  # Original text from OCR
                "ocr_pos_hash": {"type": "text"},  # Hash for OCR position
                "vehicle_id": {"type": "long"},  # Reference to vehicle
                "part_id": {"type": "long"},  # Reference to part
                "part_image_id": {"type": "long"},  # Reference to part image
                "coordinate": {"type": "text"},  # Coordinates of the OCR
                "status": {"type": "integer"},  # Status of the OCR
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
                "status_api": {"type": "integer"},  # API status
            }
        }
    }
    es.indices.create(index="part_image_ocrs", body=part_image_ocrs_mapping, ignore=400)

    part_images_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "long"},  # Unique identifier
                "name": {"type": "text"},  # Name of the part image
                "vehicle_id": {"type": "long"},  # Reference to vehicle
                "part_id": {"type": "long"},  # Reference to part
                "image": {"type": "long"},  # Reference to the image
                "media_ocr_id": {"type": "long"},  # Reference to media OCR
                "spatie_image_id": {"type": "long"},  # Reference to Spatie image
                "percentage": {"type": "integer"},  # Percentage value
                "status_api": {"type": "integer"},  # API status
                "status": {"type": "integer"},  # Status of the image
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
                "deleted_at": {"type": "date"},  # Deletion timestamp
            }
        }
    }
    es.indices.create(index="part_images", body=part_images_mapping, ignore=400)

    part_number_car_has_variants_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "long"},  # Unique identifier
                "part_number_car_id": {"type": "long"},  # Reference to part number car
                "value": {"type": "text"},  # The value associated with the variant
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
                "part_number_car_alternate_id": {"type": "text"},  # Alternate ID for part number car
            }
        }
    }
    es.indices.create(index="part_number_car_has_variants", body=part_number_car_has_variants_mapping, ignore=400)

    part_number_cars_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "long"},  # Unique identifier
                "code": {"type": "text"},  # Code associated with the part number
                "part_number": {"type": "text"},  # The part number
                "stock": {"type": "long"},  # Stock quantity
                "price": {"type": "long"},  # Price of the part
                "product_category_id": {"type": "long"},  # Reference to product category
                "product_type": {"type": "text"},  # Type of product
                "name": {"type": "text"},  # Name of the part
                "description": {"type": "text"},  # Description of the part
                "remarks": {"type": "text"},  # Remarks about the part
                "colour": {"type": "text"},  # Colour of the part
                "is_warranty": {"type": "boolean"},  # Warranty status
                "reference_code": {"type": "text"},  # Reference code for the part
                "year": {"type": "text"},  # Year of the part
                "part_label": {"type": "text"},  # Label for the part
                "alternatif_part_number": {"type": "text"},  # Alternative part number
                "model_code": {"type": "text"},  # Model code
                "supplier_code": {"type": "text"},  # Supplier code
                "alternatif_part_name": {"type": "text"},  # Alternative part name
                "is_manually_input": {"type": "integer"},  # Manual input status
                "meta": {"type": "text"},  # Additional metadata
                "updated_stock_at": {"type": "date"},  # Last updated stock timestamp
                "api_last_checked": {"type": "date"},  # Last checked timestamp from API
                "api_last_modified_value": {"type": "date"},  # Last modified value timestamp from API
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
                "deleted_at": {"type": "date"},  # Deletion timestamp
            }
        }
    }
    if not es.indices.exists(index="part_number_cars"):
        es.indices.create(index="part_number_cars", body=part_number_cars_mapping)
    else:
        print("Index 'part_number_cars' already exists.")

    vehicle_has_model_years_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "long"},  # Unique identifier
                "vehicle_id": {"type": "long"},  # Reference to vehicle
                "value": {"type": "text"},  # The model year value
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
            }
        }
    }

    if not es.indices.exists(index="vehicle_has_model_years"):
        es.indices.create(index="vehicle_has_model_years", body=vehicle_has_model_years_mapping)
    else:
        print("Index 'vehicle_has_model_years' already exists.")

    vehicle_has_production_years_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "long"},  # Unique identifier
                "vehicle_id": {"type": "long"},  # Reference to vehicle
                "value": {"type": "text"},  # The production year value
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
            }
        }
    }
    es.indices.create(index="vehicle_has_production_years", body=vehicle_has_production_years_mapping, ignore=400)

    vehicle_has_source_of_truths_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "long"},  # Unique identifier
                "vehicle_id": {"type": "long"},  # Reference to vehicle
                "path": {"type": "text"},  # Path to the source of truth
                "data": {"type": "text"},  # Data associated with the source of truth
                "summary": {"type": "text"},  # Summary of the source of truth
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
            }
        }
    }
    es.indices.create(index="vehicle_has_source_of_truths", body=vehicle_has_source_of_truths_mapping, ignore=400)

    vehicle_has_variants_mapping = {
        "mappings": {
            "properties": {
                "id": {"type": "long"},  # Unique identifier
                "vehicle_id": {"type": "long"},  # Reference to vehicle
                "value": {"type": "text"},  # The variant value
                "meta": {"type": "text"},  # Additional metadata
                "created_at": {"type": "date"},  # Creation timestamp
                "updated_at": {"type": "date"},  # Update timestamp
            }
        }
    }
    es.indices.create(index="vehicle_has_variants", body=vehicle_has_variants_mapping, ignore=400)



def index_media(media_id: int, media_data: dict):
    """Index a part record in Elasticsearch."""
    # Prepare the data to include the suggest field
    media_data['suggest'] = {
        "input": [media_data['name']],  # Use the name for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="media", id=media_id, body=media_data)

def delete_media_from_elasticsearch(media_id: int):
    """Delete a part record from Elasticsearch."""
    es.delete(index="media", id=media_id)

def index_media_ocrs(media_ocrs_id: int, media_ocrs_data: dict):
    """Index a part record in Elasticsearch."""
    # Prepare the data to include the suggest field
    media_ocrs_data['suggest'] = {
        "input": [media_ocrs_data['name']],  # Use the name for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="media_ocrs", id=media_ocrs_id, body=media_ocrs_data)

def get_media_by_ids(media_ids):
    """Fetch media records for given IDs."""
    if not media_ids:
        return []

    # Fetch media records from Elasticsearch based on the IDs
    media_query = {
        "query": {
            "terms": {
                "id": media_ids  # Use the media IDs to fetch records
            }
        }
    }

    media_results = es.search(index="media", body=media_query)
    return [hit['_source'] for hit in media_results['hits']['hits']]

def index_part(part_id: int, part_data: dict):
    """Index a part record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_data['suggest'] = {
        "input": [part_data['name']],  # Use the name for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="parts", id=part_id, body=part_data)


def delete_part_from_elasticsearch(part_id: int):
    """Delete a part record from Elasticsearch."""
    es.delete(index="parts", id=part_id)

def index_part_images(part_image_id: int, part_image_data: dict):
    """Index a part record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_image_data['suggest'] = {
        "input": [part_image_data['name']],  # Use the name for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="parts", id=part_image_id, body=part_image_data)

def delete_part_image_from_elasticsearch(part_image_id: int):
    """Delete a part record from Elasticsearch."""
    es.delete(index="part_images", id=part_image_id)

def index_part_categories(part_category_id: int, part_category_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_category_data['suggest'] = {
        "input": [part_category_data['name']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_categories", id=part_category_id, body=part_category_data)

def delete_part_category_from_elasticsearch(part_category_id: int):
    """Delete a vehicle record from Elasticsearch."""
    es.delete(index="part_categories", id=part_category_id)

def index_part_groups(part_group_id: int, part_group_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_group_data['suggest'] = {
        "input": [part_group_data['name']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_groups", id=part_group_id, body=part_group_data)

def index_part_images(part_image_id: int, part_image_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_image_data['suggest'] = {
        "input": [part_image_data['name']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_images", id=part_image_id, body=part_image_data)

def index_part_image_ocrs(part_image_ocrs_id: int, part_image_ocrs_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_image_ocrs_data['suggest'] = {
        "input": [part_image_ocrs_data['code']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_image_ocrs", id=part_image_ocrs_id, body=part_image_ocrs_data)

def index_part_number_cars(part_number_cars_id: int, part_number_cars_data: dict):
    """Index a part number car record in Elasticsearch."""

    # Convert is_warranty to boolean if it exists
    if 'is_warranty' in part_number_cars_data:
        # Convert '0' or '1' strings to boolean
        part_number_cars_data['is_warranty'] = part_number_cars_data['is_warranty'] in ['1', True]

    part_number_cars_data['suggest'] = {
        "input": [part_number_cars_data['name']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_number_cars", id=part_number_cars_id, body=part_number_cars_data)

def index_part_image_ocr_has_part_number_cars(part_image_ocr_has_part_number_cars_id: int, part_image_ocr_has_part_number_cars_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_image_ocr_has_part_number_cars_data['suggest'] = {
        "input": [part_image_ocr_has_part_number_cars_data['code']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_image_ocr_has_part_number_cars", id=part_image_ocr_has_part_number_cars_id, body=part_image_ocr_has_part_number_cars_data)

def index_part_has_vehicles(part_has_vehicles_id: int, part_has_vehicles_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_has_vehicles_data['suggest'] = {
        "input": [part_has_vehicles_data['meta']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_has_vehicles", id=part_has_vehicles_id, body=part_has_vehicles_data)


def index_part_has_vehicle_has_variants(part_has_vehicle_has_variants_id: int, part_has_vehicle_has_variants_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_has_vehicle_has_variants_data['suggest'] = {
        "input": [part_has_vehicle_has_variants_data['value']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_has_vehicle_has_variants", id=part_has_vehicle_has_variants_id, body=part_has_vehicle_has_variants_data)

def index_part_has_vehicle_has_model_years(part_has_vehicle_has_model_years_id: int, part_has_vehicle_has_model_years_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_has_vehicle_has_model_years_data['suggest'] = {
        "input": [part_has_vehicle_has_model_years_data['value']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_has_vehicle_has_model_years", id=part_has_vehicle_has_model_years_id, body=part_has_vehicle_has_model_years_data)

def index_part_has_vehicle_has_production_years(part_has_vehicle_has_production_years_id: int, part_has_vehicle_has_production_years_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_has_vehicle_has_production_years_data['suggest'] = {
        "input": [part_has_vehicle_has_production_years_data['value']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_has_vehicle_has_production_years", id=part_has_vehicle_has_production_years_id, body=part_has_vehicle_has_production_years_data)

def index_part_number_car_has_variants(part_number_car_has_variants_id: int, part_number_car_has_variants_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    part_number_car_has_variants_data['suggest'] = {
        "input": [part_number_car_has_variants_data['value']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="part_number_car_has_variants", id=part_number_car_has_variants_id, body=part_number_car_has_variants_data)

def index_vehicle_has_model_years(vehicle_has_model_years_id: int, vehicle_has_model_years_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    vehicle_has_model_years_data['suggest'] = {
        "input": [vehicle_has_model_years_data['value']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="vehicle_has_model_years", id=vehicle_has_model_years_id, body=vehicle_has_model_years_data)

def index_vehicle_has_production_years(vehicle_has_production_years_id: int, vehicle_has_production_years_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    vehicle_has_production_years_data['suggest'] = {
        "input": [vehicle_has_production_years_data['value']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="vehicle_has_production_years", id=vehicle_has_production_years_id, body=vehicle_has_production_years_data)

def index_vehicle_has_variants(vehicle_has_variants_id: int, vehicle_has_variants_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    vehicle_has_variants_data ['suggest'] = {
        "input": [vehicle_has_variants_data['value']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="vehicle_has_variants", id=vehicle_has_variants_id, body=vehicle_has_variants_data)

def index_vehicle_has_source_of_truths(vehicle_has_source_of_truths_id: int, vehicle_has_source_of_truths_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    vehicle_has_source_of_truths_data['suggest'] = {
        "input": [vehicle_has_source_of_truths_data['data']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="vehicle_has_source_of_truths", id=vehicle_has_source_of_truths_id, body=vehicle_has_source_of_truths_data)

def index_vehicle(vehicle_id: int, vehicle_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    vehicle_data['suggest'] = {
        "input": [vehicle_data['title']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="vehicles", id=vehicle_id, body=vehicle_data)

def index_vehicle_has_variant_(vehicle_has_variant_id: int, vehicle_has_variant_data: dict):
    """Index a vehicle record in Elasticsearch."""
    # Prepare the data to include the suggest field
    vehicle_has_variant_data['suggest'] = {
        "input": [vehicle_has_variant_data['title']],  # Use the title for suggestions
        "weight": 1  # Optional: you can set a weight for the suggestion
    }
    es.index(index="vehicle_has_variants", id=vehicle_has_variant_id, body=vehicle_has_variant_data)


def delete_vehicle_from_elasticsearch(vehicle_id: int):
    """Delete a vehicle record from Elasticsearch."""
    es.delete(index="vehicles", id=vehicle_id)


def search_global(query: str, page: int = 1, page_size: int = 10):
    """Search for vehicles and parts globally with suggestions and pagination."""

    # Get the current timestamp
    timestamp = datetime.utcnow().isoformat() + "Z"

    # Check if the query is empty
    if not query:
        return JSONResponse(
            content={
                "status": "error",
                "data": None,
                "message": "Query cannot be empty.",
                "errors": [
                    {
                        "code": "MISSING_FIELD",
                        "message": "The 'query' field is required."
                    }
                ],
                "timestamp": timestamp
            },
            status_code=400  # HTTP status code for bad request
        )

    # Calculate the starting index for pagination
    from_index = (page - 1) * page_size

    # Search for vehicles with fuzzy matching
    vehicle_search_query = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "description", "model"],  # Boost title field
                "fuzziness": "AUTO"  # Enable fuzzy matching
            }
        },
        "from": from_index,
        "size": page_size  # Limit the number of results returned
    }

    # Search for parts with fuzzy matching
    part_search_query = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name", "description","meta","code"],  # Boost name field
                "fuzziness": "AUTO"  # Enable fuzzy matching
            }
        },
        "from": from_index,
        "size": page_size  # Limit the number of results returned
    }

    # Execute the search
    vehicle_results = es.search(index="vehicles", body=vehicle_search_query)
    part_results = es.search(index="parts", body=part_search_query)

    # Combine results into a single list
    combined_results = {
        "vehicles": vehicle_results['hits']['hits'],
        "parts": part_results['hits']['hits'],
        "combined": []  # This will hold the combined results
    }

    # Collect media IDs for vehicles and parts
    media_ids = []
    suggestions = []  # List to hold all suggestions

    # Combine vehicles and parts into a single list
    for vehicle in combined_results['vehicles']:
        vehicle_data = vehicle['_source']
        media_ids.append(vehicle_data['image'])  # Collect image ID for media
        combined_results['combined'].append({
            "type": "vehicle",
            "data": vehicle_data
        })
        # Collect suggestions
        suggestions.append(vehicle_data['suggest']['input'][0])  # Assuming input is a list

    for part in combined_results['parts']:
        part_data = part['_source']
        media_ids.append(part_data['image'])  # Collect image ID for media
        combined_results['combined'].append({
            "type": "part",
            "data": part_data
        })
        # Collect suggestions
        suggestions.append(part_data['suggest']['input'][0])  # Assuming input is a list

    # Fetch media records based on collected media IDs
    media_records = get_media_by_ids(media_ids)

    # Map media records to their respective vehicles and parts
    media_map = {media['id']: media for media in media_records}

    # Add media information to vehicles and parts
    for vehicle in combined_results['combined']:
        if vehicle['type'] == "vehicle":
            vehicle['data']['media'] = media_map.get(vehicle['data']['image'], None)  # Add media if exists
        elif vehicle['type'] == "part":
            vehicle['data']['media'] = media_map.get(vehicle['data']['image'], None)  # Add media if exists

    # Check if there are results and return the appropriate response
    if not combined_results['combined']:
        return JSONResponse(
            content={
                "status": "error",
                "data": None,
                "message": "No results found.",
                "timestamp": timestamp
            },
            status_code=404  # HTTP status code for not found
        )

    # Sort suggestions in ascending order and remove duplicates
    unique_suggestions = sorted(set(suggestions))

    return JSONResponse(
        content={
            "status": "success",
            "data": {
                "results": combined_results['combined'],
                "suggestions": unique_suggestions,  # Include sorted suggestions
                "total_count": len(combined_results['combined'])  # Total count of results
            },
            "message": "Search completed successfully.",
            "timestamp": timestamp
        },
        status_code=200  # HTTP status code for success
    )

def suggestion_global(query: str, page: int = 1, page_size: int = 10):
    """Suggest for vehicles and parts globally with suggestions and pagination."""

    # Get the current timestamp
    timestamp = datetime.utcnow().isoformat() + "Z"

    # Check if the query is empty
    if not query:
        return JSONResponse(
            content={
                "status": "error",
                "data": None,
                "message": "Query cannot be empty.",
                "errors": [
                    {
                        "code": "MISSING_FIELD",
                        "message": "The 'query' field is required."
                    }
                ],
                "timestamp": timestamp
            },
            status_code=400  # HTTP status code for bad request
        )

    # Calculate the starting index for pagination
    from_index = (page - 1) * page_size

    # Search for vehicles with fuzzy matching
    vehicle_search_query = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "description", "model"],  # Boost title field
                "fuzziness": "AUTO"  # Enable fuzzy matching
            }
        },
        "from": from_index,
        "size": page_size  # Limit the number of results returned
    }

    # Search for parts with fuzzy matching
    part_search_query = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name", "description","meta","code"],  # Boost name field
                "fuzziness": "AUTO"  # Enable fuzzy matching
            }
        },
        "from": from_index,
        "size": page_size  # Limit the number of results returned
    }

    # Execute the search
    vehicle_results = es.search(index="vehicles", body=vehicle_search_query)
    part_results = es.search(index="parts", body=part_search_query)

    # Combine results into a single list
    combined_results = {
        "vehicles": vehicle_results['hits']['hits'],
        "parts": part_results['hits']['hits'],
        "combined": []  # This will hold the combined results
    }

    # Collect media IDs for vehicles and parts
    media_ids = []
    suggestions = []  # List to hold all suggestions

    # Combine vehicles and parts into a single list
    for vehicle in combined_results['vehicles']:
        vehicle_data = vehicle['_source']
        media_ids.append(vehicle_data['image'])  # Collect image ID for media
        combined_results['combined'].append({
            "type": "vehicle",
            "data": vehicle_data
        })
        # Collect suggestions
        suggestions.append(vehicle_data['suggest']['input'][0])  # Assuming input is a list

    for part in combined_results['parts']:
        part_data = part['_source']
        media_ids.append(part_data['image'])  # Collect image ID for media
        combined_results['combined'].append({
            "type": "part",
            "data": part_data
        })
        # Collect suggestions
        suggestions.append(part_data['suggest']['input'][0])  # Assuming input is a list

    # Fetch media records based on collected media IDs
    media_records = get_media_by_ids(media_ids)

    # Map media records to their respective vehicles and parts
    media_map = {media['id']: media for media in media_records}

    # Add media information to vehicles and parts
    for vehicle in combined_results['combined']:
        if vehicle['type'] == "vehicle":
            vehicle['data']['media'] = media_map.get(vehicle['data']['image'], None)  # Add media if exists
        elif vehicle['type'] == "part":
            vehicle['data']['media'] = media_map.get(vehicle['data']['image'], None)  # Add media if exists

    # Check if there are results and return the appropriate response
    if not combined_results['combined']:
        return JSONResponse(
            content={
                "status": "error",
                "data": None,
                "message": "No results found.",
                "timestamp": timestamp
            },
            status_code=404  # HTTP status code for not found
        )

    # Sort suggestions in ascending order and remove duplicates
    unique_suggestions = sorted(set(suggestions))

    return JSONResponse(
        content={
            "status": "success",
            "data": {
                "suggestions": unique_suggestions,  # Include sorted suggestions
            },
            "message": "Search completed successfully.",
            "timestamp": timestamp
        },
        status_code=200  # HTTP status code for success
    )