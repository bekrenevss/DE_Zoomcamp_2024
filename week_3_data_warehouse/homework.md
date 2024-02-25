## Question 1

What is count of records for the 2022 Green Taxi Data??

840402

SELECT count(*) FROM `de-zoomcamp-2024-411915.ny_taxi.external_yellow_tripdata`

## Question 2

Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

0 MB for the External Table and 6.41MB for the Materialized Table

SELECT COUNT(DISTINCT PULocationID)
FROM de-zoomcamp-2024-411915.ny_taxi.green_tripdata_2022_non_partitioned;

SELECT COUNT(DISTINCT PULocationID)
FROM de-zoomcamp-2024-411915.ny_taxi.external_green_tripdata_2022;

## Question 3

How many records have a fare_amount of 0?

1622

SELECT COUNT(*)
FROM de-zoomcamp-2024-411915.ny_taxi.green_tripdata_2022_non_partitioned
WHERE fare_amount = 0;

## Question 4

What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)

Partition by lpep_pickup_datetime Cluster on PUlocationID

## Question 5

Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?

Choose the answer which most closely matches.

SELECT count(distinct PULocationID)
FROM de-zoomcamp-2024-411915.ny_taxi.green_tripdata_2022_non_partitioned
WHERE
  lpep_pickup_datetime >= '2022-06-01'
  and lpep_pickup_datetime <= '2022-06-30'
-- 12,82 Mb

SELECT count(distinct PULocationID)
FROM de-zoomcamp-2024-411915.ny_taxi.green_tripdata_2022_partitioned
WHERE
  lpep_pickup_datetime >= '2022-06-01'
  and lpep_pickup_datetime <= '2022-06-30'
-- 1.12 Mb

12.82 MB for non-partitioned table and 1.12 MB for the partitioned table


## Questuon 6

Where is the data stored in the External Table you created?

GCP Bucket

## Qyestion 7

It is best practice in Big Query to always cluster your data:

False