import os
import json
import glob
import sys
import logging
from resource_mapper import ResourceMapper

# Function to process FHIR resources from JSON files
def process_fhir_resources(directory):
    resources = {}
    json_files = glob.glob(os.path.join(directory, '*.ndjson'))
    for file_path in json_files:
        logging.info(f'Processing {file_path}')
        with open(file_path, 'r') as file:
            for line in file:
                resource_json = json.loads(line)
                tyyp, resource = ResourceMapper.map(resource_json)
                if resource:
                    if tyyp not in resources:
                        resources[tyyp] = []
                    resources[tyyp].append(resource)
                logging.info(f'Loaded {tyyp} resource with ID: {resource.id}')
    return resources

# Example usage
if __name__ == "__main__":
    # Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
    logging.getLogger().setLevel(logging.NOTSET)

    # Add stdout handler, with level INFO
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-13s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    directory_path = './../../data/extracted'
    resources = process_fhir_resources(directory_path)
    # print the number of resources loaded by type
    for resource_type, resources in resources.items():
        logging.info(f'{resource_type}: {len(resources)}')
    logging.info('Processing complete')
