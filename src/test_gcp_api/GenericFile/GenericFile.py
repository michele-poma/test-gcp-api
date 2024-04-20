import pandas as pd

class JsonFile():
    def __init__(self, filename, extension, project, bucket, path):
        self.filename = filename
        self.extension = extension
        self.project = project
        self.bucket = bucket
        self.path = path

    def file_exist(self,filename):
        pass

    def readFile(self,filename):
        input_df = pd.read_json(filename)
        return input_df