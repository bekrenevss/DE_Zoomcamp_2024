-- This code creates an external table named `de-zoomcamp-2024-411915.ny_taxi.external_yellow_tripdata` 
-- that is stored in the PARQUET format. The table is linked to the Google Cloud Storage (GCS) bucket 
-- `gs://dezoomcamp2024/trip-data/green_tripdata_2022-*.parquet`, which contains the trip data files.
-- The external table allows querying the data in the GCS bucket without the need to load it into BigQuery.
CREATE OR REPLACE EXTERNAL TABLE `de-zoomcamp-2024-411915.ny_taxi.external_yellow_tripdata`
OPTIONS (
        format = 'PARQUET',
        uris = ['gs://dezoomcamp2024/trip-data/green_tripdata_2022-*.parquet']
    )
