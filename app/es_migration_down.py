import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Get all indices
es=os.getenv("ELASTICSEARCH_LOCAL")
response = requests.get(f"{es}/_cat/indices?v")
indices = response.text.splitlines()[1:]  # Skip the header

# Delete each index
for index in indices:
    index_name = index.split()[2]  # Get the index name
    delete_response = requests.delete(f"{es}/{index_name}")
    print(f"Deleted index: {index_name}, Response: {delete_response.status_code}")