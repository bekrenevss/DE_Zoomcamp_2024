variable "credentials" {
    description = "My Credentials"
    default = "/workspaces/DE_Zoomcamp_2024/week_1_basics_n_setup/1_terraform_gcp/keys/my-creds.json"
}
variable "project" {
    description = "Project"
    default = "de-zoomcamp-2024-411915"
}

variable "region" {
    description = "Region"
    default = "s-central1"
}

variable "location" {
    description = "Project Location"
    default = "US"
}

variable "bq_dataset_name" {
    description = "My BigQuery Dataset Name"
    default = "second_dataset"
}

variable "gcs_bucket_name" {
    description = "My Storage Bucket Name"
    default = "de-zoomcamp-2024-411915-terra-bucket"
}

variable "gcs_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"
}