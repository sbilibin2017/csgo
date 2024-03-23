#!/bin/bash 
 
echo "Waiting for postgres..." 
while ! nc -z csgo_postgres 5432; do 
  sleep 1 
done 
echo "Postgres started" 
 
echo "Waiting for clickhouse..." 
while ! nc -z csgo_clickhouse 9000; do 
  sleep 1 
done 
echo "Clickhouse started" 
 
uvicorn main:app --host 0.0.0.0 --port 8000 