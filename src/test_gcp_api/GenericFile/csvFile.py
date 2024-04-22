import pandas as pd

from test_gcp_api.genericFile.genericFile import GenericFile

class CsvFile(GenericFile):
    def __init__(self, filename, extension, project, bucket, path):
        super.__init__()

    def file_exist(self,filename):
        pass

    def readFile(self,filename):
        pass