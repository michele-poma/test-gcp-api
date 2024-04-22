from google.cloud import storage

import json


class CloudStorage:
    """Cloud Storage Handler"""

    def __init__(self, bucket_name, project):
        self.client = storage.Client()
        self.bucket = self.client.get_bucket(bucket_name)

    def exists(self, filename):
        """Check if a blob exists"""
        if self.bucket.get_blob(filename):
            return True
        else:
            return False

    def get_bucket_list(self):
        return self.client.list_buckets()

    def get_content(self, remote_filename):
        """Download remote file"""
        blob = self.bucket.blob(remote_filename)
        data = blob.download_as_string()
        return data

    def get_content_json(self, remote_filename):
        """Download remote file"""
        blob = self.bucket.blob(remote_filename)
        data = blob.download_as_string()
        dict_result = json.loads(data)
        return dict_result


    def rename(self, filename, newname):
        """Rename a file"""
        blob = self.bucket.blob(filename)
        self.bucket.rename_blob(blob, newname)

    def upload_file(self, local_filename, remote_filename):
        """Upload a local file"""
        blob = self.bucket.blob(remote_filename)
        blob.upload_from_filename(filename=local_filename)

    def download(self, remote_filename, local_filename=None):
        """Download remote file"""
        if local_filename is None:
            local_filename = remote_filename
        blob = self.bucket.blob(remote_filename)
        blob.download_to_filename(local_filename)
