import pyarrow.parquet as pq
import requests
import pandas as pd
import gcsfs

# Define the base URL and file pattern
base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'
file_pattern = 'fhv_tripdata_2020-{:02}.parquet'

# Initialize a GCS filesystem
fs = gcsfs.GCSFileSystem(project='de-zoomcamp-2024-411915')

# Define the GCS bucket and file path
bucket = 'dezoomcamp2024'
# file_path = 'trip-data/green_tripdata_2022-01.parquet'

def copy_file_from_url_to_gcs(url, bucket, file_path):
    # Download the file from the URL
    response = requests.get(url)
    # Write the file to the GCS bucket
    with fs.open(f'{bucket}/{file_path}', 'wb') as f:
        f.write(response.content)

# Loop over the months
for month in range(1, 13):
    # Create the URL and filename
    filename = file_pattern.format(month)
    url = base_url + filename
    folder = 'fhv'
    copy_file_from_url_to_gcs(url, bucket, f'{folder}/{filename}')
    print(f"File {filename} copy successfully")


        
# def download_file(url, folder, filename):
#     response = requests.get(url, stream=True)
#     with open(f'{folder}/{filename}', 'wb') as out_file:
#         out_file.write(response.content)
#     print(f"File {filename} downloaded successfully")



# Loop over the months
# for month in range(1, 13):
#     # Create the URL and filename
#     url = base_url + file_pattern.format(month)
#     folder = 'trip-data'
#     filename = file_pattern.format(month)
#     # Download the file
#     download_file(url, folder, filename)
#     print(f"File {filename} downloaded successfully")
