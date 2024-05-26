# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# ... other Dockerfile instructions ...

# Define the output directory within the container
RUN mkdir -p /data/output

# Mount the host directory as a volume
VOLUME ["/data/output"]

# ... other Dockerfile instructions ...

# (Optional) Modify your script to write to /data/output/output.csv
# This assumes your script writes the CSV to the working directory by default.
CMD ["python3", "csv_gen.py", "/data/output/output.csv"]


# Command to run the application (optional, you can customize this)
#ENTRYPOINT ["python3"]
#CMD [ "csv_gen.py" ]
