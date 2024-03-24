#!/bin/bash 

while ! nc -z csgo_postgres 5432; do 
  echo "Waiting for postgres..." 
  sleep 1 
done 
echo "Postgres started" 
 
while ! nc -z csgo_clickhouse 9000; do 
  echo "Waiting for clickhouse..." 
  sleep 1 
done 
echo "Clickhouse started" 
 
uvicorn main:app --host 0.0.0.0 --port 8000 