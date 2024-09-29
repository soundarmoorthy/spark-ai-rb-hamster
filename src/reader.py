import os
import json
import glob
import logging
from resource_mapper import ResourceMapper
from src import BASE_DIR


# Function to process FHIR resources from JSON files
def process_fhir_resources(directory):
    resources = {}
    # recursively look for all ndjson files in the directory. look into sub directories
    json_files = glob.glob(f'{directory}/**/*.ndjson', recursive=True)
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
            logging.info(f'Completed {file_path}')
    return resources

# Example usage
if __name__ == "__main__":
    # Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
    directory_path = os.path.join(BASE_DIR, 'extracted')
    resources = process_fhir_resources(directory_path)
    # print the number of resources loaded by type
    for resource_type, resources in resources.items():
        logging.info(f'{resource_type}: {len(resources)}')
    logging.info('Processing complete')
