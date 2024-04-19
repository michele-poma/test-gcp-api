import logging

from google.cloud import storage

from test_gcp_api.storage_classes.CloudStorage import CloudStorage
from test_gcp_api.storage_classes.BigQueryStorage import BigQueryStorage


def main():
    dataset="test_mic"

    cloud_storage = CloudStorage("test-gcp-api","training-gcp")
    file_exist = cloud_storage.exists("test.txt")
    logging.info("file: %s exist? %s","test.txt", file_exist)

    bq = BigQueryStorage("training-gcp-309207","EU")
    dataset_exist = bq.dataset_exist(dataset)
    logging.error("dataset: {} is present? {}".format(dataset, dataset_exist))

if __name__ == "__main__":
    main()

