import polars as pl
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the secret from environment variables
secret_key = os.getenv('MY_SECRET_KEY')

# Example use of the secret_key (e.g., for an API request)
print(f"My secret key is: {secret_key}")

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28]
}
df = pl.DataFrame(data)

# Write the DataFrame to a CSV file
output_folder = "/data/output"

df.write_csv(f"{output_folder}/output.csv")

print("CSV file created successfully!")
