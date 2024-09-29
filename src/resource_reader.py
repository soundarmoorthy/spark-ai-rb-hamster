

import os
import json
import glob
from fhirclient import client
import fhirclient

# Function to read NDJSON data from a file
def read_ndjson_file(file_path):
    with open(file_path, 'r') as file:
        return [json.loads(line) for line in file]

# Function to process FHIR resources from NDJSON files
def process_fhir_resources(directory):
    resource_dict = {}
    ndjson_files = glob.glob(os.path.join(directory, '*.ndjson'))
    for file_path in ndjson_files:
        resources = read_ndjson_file(file_path)
        for resource in resources:
            resource_type = resource.get('resourceType')
            if resource_type:
                fhir_resource_class = getattr(fhirclient.models, resource_type.lower(), None)
                if fhir_resource_class:
                    fhir_resource = fhir_resource_class(resource, strict=False)
                    if resource_type not in resource_dict:
                        resource_dict[resource_type] = []
                    resource_dict[resource_type].append(fhir_resource)
    return resource_dict

# Example usage
if __name__ == "__main__":
    directory_path = './../../data/extracted'
    resource_dict = process_fhir_resources(directory_path)
    for resource_type, resources in resource_dict.items():
        print(f'{resource_type}: {len(resources)}')