import pandas as pd

class GenericFile():
    def __init__(self, filename, extension, project, bucket, path):
        self.filename = filename
        self.extension = extension
        self.project = project
        self.bucket = bucket
        self.path = path

    def file_exist(self,filename):
        pass

    def readFile(self,filename):
        pass