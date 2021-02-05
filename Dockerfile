# Base image
FROM postgres:10-alpine

# Set database parameters
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=user
ENV POSTGRES_DB=database

# Add CSV files for loading
ADD docker/data/*.csv /docker-entrypoint-initdb.d/data/

# Add SQL statements to set up database
ADD docker/*.sql /docker-entrypoint-initdb.d/