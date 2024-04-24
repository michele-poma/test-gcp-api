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

    filename = inputFile.filename
    extension = inputFile.extension
    project = inputFile.project
    bucket = inputFile.bucket
    path = inputFile.path

    gcp_file = path+"/"+filename+"."+extension
    logging.info("\n\n****** Get bucket list by Cloud Storage API ******")
    cloud_storage = CloudStorage(bucket,project)
    bucket_list = cloud_storage.get_bucket_list()

    for bucket in bucket_list: #cloud_storage.client.list_buckets():
        logging.info(bucket.name)

    logging.info("********************************************************")
    logging.info("\n\n****** Use Cloud Storage API to check if bucket exists ******")
    file_exist = cloud_storage.exists(gcp_file)
    logging.info("file: %s exist? %s",gcp_file, file_exist)
    logging.info("********************************************************")

    #TODO USE ENCODER/DECODER
    if file_exist:
        input_data_conf = cloud_storage.get_content_json(gcp_file)[0]
        logging.info(input_data_conf)
    else:
        logging.warning("file: %s doesn t exist!!!", gcp_file)

    bq_filename = input_data_conf['filename']
    bq_file_extension = input_data_conf['extension']
    bq_file_created = input_data_conf['created']
    bq_project = input_data_conf['bq_project']
    bq_bucket = input_data_conf['bucket']
    bq_path = input_data_conf['path']
    bq_dataset = input_data_conf['dataset']
    bq_table = input_data_conf['table']
    bq_dag = input_data_conf['dag']

    #bq = BigQueryStorage("training-gcp-309207","EU")
    bq = BigQueryStorage(bq_project,"EU")
    dataset_exist = bq.dataset_exist(bq_dataset)
    #logging.error("bq_dataset: {} is present? {}".format(bq_dataset, dataset_exist))
    if not dataset_exist:
        bq.create_dataset(bq_dataset)
        dataset_created_exist = bq.dataset_exist(bq_dataset)
        logging.info("bq_dataset: {} is present? {}".format(bq_dataset, dataset_created_exist))

    bq.delete_dataset(bq_dataset)
    logging.info("bq_dataset: %s exist? %s",bq_dataset,bq.dataset_exist(bq_dataset))


if __name__ == "__main__":
    main()

