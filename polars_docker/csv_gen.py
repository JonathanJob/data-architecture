import polars as pl

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28]
}
df = pl.DataFrame(data)

# Write the DataFrame to a CSV file
df.write_csv("output.csv")

print("CSV file created successfully!")
