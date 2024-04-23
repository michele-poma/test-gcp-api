import logging
import pandas as pd

from google.cloud import storage

from test_gcp_api.storage_classes.CloudStorage import CloudStorage
from test_gcp_api.storage_classes.BigQueryStorage import BigQueryStorage
from test_gcp_api.genericFile.jsonFile import JsonFile
from test_gcp_api.genericFile.genericFile import GenericFile
import test_gcp_api.utils.util  as u


def main():

    logging.basicConfig(level = logging.INFO)

    logging.info("********** Reading file configuration **********")
    df = u.read_json_file("configuration/conf.json")
    a = [df[i] if (df[i].get('filename')=='input_conf') else df[0] for i in range(len(df))][0]

    #TODO USE ENCODER/DECODER
    inputFile = JsonFile(a.get('filename',None), a.get('extension',None), a.get('project',None), a.get('bucket',None), a.get('path',None))

    logging.info("********************************************************")
    logging.info("* Variable Set:                        ")
    logging.info("*               FileName: %s           ", inputFile.filename)
    logging.info("*               extension: %s          ", inputFile.extension)
    logging.info("*               project: %s            ", inputFile.project)
    logging.info("*               bucket: %s             ", inputFile.bucket)
    logging.info("*               path: %s               ", inputFile.path)
    logging.info("********************************************************")


    gcp_file = inputFile.path+"/"+inputFile.filename+"."+inputFile.extension
    logging.info("\n\n****** Get bucket list by Cloud Storage API ******")
    cloud_storage = CloudStorage(inputFile.bucket,inputFile.project)
    bucket_list = cloud_storage.get_bucket_list()

    for bucket in bucket_list: #cloud_storage.client.list_buckets():
        logging.info(bucket.name)

    logging.info("********************************************************")
    logging.info("\n\n****** Use Cloud Storage API to check if bucket exists ******")
    file_exist = cloud_storage.exists(gcp_file)
    logging.info("file: %s exist? %s","test.txt", file_exist)
    logging.info("********************************************************")

    #TODO USE ENCODER/DECODER
    if file_exist:
        input_data_conf = cloud_storage.get_content_json(gcp_file)[0]
    else:
        logging.warning("file: %s doesn t exist!!!", gcp_file)


    bq = BigQueryStorage("training-gcp-309207","EU")
    dataset_exist = bq.dataset_exist(dataset)
    #logging.error("dataset: {} is present? {}".format(dataset, dataset_exist))
    if not dataset_exist:
        bq.create_dataset(dataset)
        dataset_created_exist = bq.dataset_exist(dataset)
        logging.info("dataset: {} is present? {}".format(dataset, dataset_created_exist))

    bq.delete_dataset(dataset)
    logging.info("dataset: %s exist? %s",dataset,bq.dataset_exist(dataset))


if __name__ == "__main__":
    main()

