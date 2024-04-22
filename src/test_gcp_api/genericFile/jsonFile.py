import pandas as pd

from test_gcp_api.genericFile.genericFile import GenericFile

class JsonFile(GenericFile):
    def __init__(self, filename, extension, project, bucket, path):
        super.__init__()

    def file_exist(self,filename):
        pass

    def readFile(self,filename):
        input_df = pd.read_json(filename)
        return input_df