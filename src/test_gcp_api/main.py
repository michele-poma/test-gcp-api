import logging
import pandas as pd

from google.cloud import storage

from test_gcp_api.storage_classes.CloudStorage import CloudStorage
from test_gcp_api.storage_classes.BigQueryStorage import BigQueryStorage
from test_gcp_api.genericFile.genericFile import JsonFile
import test_gcp_api.utils.util  as u


def main():

    logging.basicConfig(level = logging.INFO)

    # df = u.get_configuration("configuration/conf.json")
    # logging.info(df.filename)
    # inputFile = JsonFile(df.filename, df.extension, df.project, df.bucket, df.path)
    #
    # i = u.read_json_file("configuration/conf.json")


    dataset="test_mic"

    cloud_storage = CloudStorage("test-gcp-api","training-gcp")

    bucket_list = cloud_storage.get_bucket_list()

    for bucket in bucket_list: #cloud_storage.client.list_buckets():
        logging.info(bucket.name)

    file_exist = cloud_storage.exists("input-conf/input_conf.json")
    f = cloud_storage.get_content_json("input-conf/input_conf.json")
    logging.error("file: %s exist? %s","test.txt", file_exist)



    bq = BigQueryStorage("training-gcp-309207","EU")
    dataset_exist = bq.dataset_exist(dataset)
    logging.error("dataset: {} is present? {}".format(dataset, dataset_exist))

if __name__ == "__main__":
    main()

