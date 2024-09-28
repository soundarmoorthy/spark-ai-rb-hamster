

import os
import json

from fhir.resources import construct_fhir_element
from pydantic import ValidationError


def parse_fhir_resources(directory):
    # dictionary of resource name and list of resources
    fhir_resources = {}
    # read the ndjson files. based on the resourceType in the json,
    # add to the dictionary
    for file in os.listdir(directory):
        if file.endswith('.ndjson'):
            with open(os.path.join(directory, file)) as f:
                for line in f:
                    try:
                        resource = json.loads(line)
                        resource_type = resource.get('resourceType')
                        if resource_type:
                            if resource_type not in fhir_resources:
                                fhir_resources[resource_type] = []
                            fhir_resources[resource_type].append(construct_fhir_element(resource_type, resource))
                    except BaseException as e:
                        print(f'Error parsing line: {line}')
                        print(e)
                        continue
    return fhir_resources

# Usage
directory = './../data/extracted'
fhir_resources = parse_fhir_resources(directory)

# Print the number of resources
for resource_type, resources in fhir_resources.items():
    print(f'{resource_type}: {len(resources)}')