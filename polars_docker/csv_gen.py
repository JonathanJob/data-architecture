import polars as pl
import os
from dotenv import load_dotenv

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
