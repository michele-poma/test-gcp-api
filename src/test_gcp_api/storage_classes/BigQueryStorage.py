import logging
from google.cloud.bigquery import Client
from google.cloud import bigquery


class BigQueryStorage:
    """
    Client to connect on BigQuery.
    """

    def __init__(self, gcp_project: str, gcp_location: str):
        self.client = bigquery.Client(project=gcp_project)


    def create_dataset(self, dataset: str):
        """
        Create dataset in BigQuery

        :param dataset_name: dataset for table
        :return:
        """
        try:
            dataset = self.client.create_dataset(dataset)
            logging.info("Dataset {} created!!".format(dataset))
        except e:
            logging.error("Dataset {} not created!!".format(dataset))

    def dataset_exist(self, dataset_name: str) -> bool:
        """
        check if dataset exist
        :param dataset_name: dataset name
        :return:
            - True if dataset exists
            - False if dataset doesn't exist
        """
        try:
            self.client.get_dataset(dataset_name)  # Make an API request.
            logging.info("Dataset %s already exists", dataset_id)
            logging.info('The run of this task refers to %s', today_date)
            return True
        except Exception as e:
            logging.warning("Dataset %s is not found",dataset_name)
            return False
    def create_table(self, tablename: str):
        """
        create the BQ table

        :param tablename: name of table
        :return:
        """
        pass

    def exist_table(self, tablename: str):
        """
        Check if table exists

        :param tablename: name of table
        :return:
        """
        pass

    def readTable(self, tablename: str):

        """
        Get all records from table

        :param tablename: name of table
        :return:
        """

        #create query
        query = "SELECT * FROM {}".FORMAT(tablename)

        #run query
        query_job = client.query(QUERY)  # API request
        rows = query_job.result()  # Waits for query to finish

        #read rows
        for row in rows:
            logging.info(row)

    def insert_data(self, data: str):
        pass

    def load_csv(self, csv_file):
        pass

