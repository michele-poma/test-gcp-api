import pandas as pd
import json

def get_configuration(filename):
    input_df = pd.read_json(filename)
    return input_df

def read_json_file(filename):
    """Read a json file"""
    with open(filename, "r+") as f:
        return json.loads(f.read())
