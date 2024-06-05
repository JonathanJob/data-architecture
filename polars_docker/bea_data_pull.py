import polars as pl
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Access the secret from environment variables
secret_key = os.getenv('BEA_SECRET_KEY')

# Example use of the secret_key (e.g., for an API request)
print(f"My secret key is: {secret_key}")

# Step 1: Define the API URL and headers
url = f'https://apps.bea.gov/api/data?&UserID={secret_key}&method=GETDATASETLIST&'
headers = {
    'Authorization': f'Bearer {secret_key}'  # Replace with your actual access token
}

# Step 2: Send an HTTP GET request to the API
response = requests.get(url, headers=headers)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the JSON response
    data = response.json()
    
    # Step 5: Convert the JSON data to a Polars DataFrame
    df = pl.DataFrame(data)
    
    # Display the DataFrame
    print(df)

    # Write the DataFrame to a CSV file
    output_folder = "/data/output"

    df.write_csv(f"{output_folder}/bea_dataset_list.csv")

    print("CSV file created successfully!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
