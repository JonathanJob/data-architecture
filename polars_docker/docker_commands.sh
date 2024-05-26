# Build the docker container
docker build -t polars-env .

# exec container
docker run -e MY_SECRET_KEY="$MY_SECRET_KEY" -v {abs_local_path}/data-architecture/polars_docker/output_data:/data/output polars-env
