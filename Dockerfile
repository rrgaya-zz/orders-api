FROM postgres:10.3-alpine

WORKDIR /code

# COPY tangotech-2020-01-10.dmp /code/
COPY tangotech.pgsql.202001181256.dmp /code/