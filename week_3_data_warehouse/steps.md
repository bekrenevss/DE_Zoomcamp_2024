-- Create an external table that refers to a GCS (Google Cloud Storage) path
CREATE OR REPLACE EXTERNAL TABLE `de-zoomcamp-2024-411915.ny_taxi.external_yellow_tripdata`
OPTIONS (
    format = 'PARQUET',
    uris = ['gs://dezoomcamp2024/trip-data/green_tripdata_2022-*.parquet']
  )

-- Create a non-partitioned table from an external table
CREATE OR REPLACE TABLE de-zoomcamp-2024-411915.ny_taxi.green_tripdata_non_partitioned AS
SELECT * FROM de-zoomcamp-2024-411915.ny_taxi.external_green_tripdata_2022;