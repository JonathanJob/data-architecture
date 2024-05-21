# Build the docker container
docker build -t polars-env .

# Start the container
docker run -it --name my-polars-container polars-env