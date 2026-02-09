import os
import yaml

def load_test_data():
    path = os.path.join(os.path.dirname(__file__), '..', 'tests', 'test_data.yaml')
    with open(path, 'r') as file:
        return yaml.safe_load(file)