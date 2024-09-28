


import unittest
import json
from pydantic import ValidationError
from fhir.resources.fhir.res import construct_fhir_element

class TestProcedure(unittest.TestCase):
    def test_procedure(self):
        try:
            resource = json.loads(data())
            resource_type = resource.get('resourceType')
            self.assertEqual(resource_type, 'Procedure')
            fhir_resource = construct_fhir_element(resource_type, resource)
            self.assertEqual(fhir_resource.resource_type, 'Procedure')
        except ValidationError as e:
            self.fail(f'ValidationError: {e}')
        except BaseException as e:
            self.fail(f'Exception: {e}')

def data():
    return """
    {
      "resourceType": "Procedure",
      "id": "5df15ef1-6eec-e000-6103-e7540e35df27",
      "meta": {
        "profile": [
          "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure"
        ]
      },
      "status": "completed",
      "code": {
        "coding": [
          {
            "system": "http://snomed.info/sct",
            "code": "710824005",
            "display": "Assessment of health and social care needs (procedure)"
          }
        ],
        "text": "Assessment of health and social care needs (procedure)"
      },
      "subject": {
        "reference": "Patient/736a19c8-eea5-32c5-67ad-1947661de21a"
      },
      "encounter": {
        "reference": "Encounter/4448de54-a525-096e-3da0-5a929f0231be"
      },
      "performedPeriod": {
        "start": "2015-06-05T18:21:10-04:00",
        "end": "2015-06-05T19:06:57-04:00"
      },
      "location": {
        "reference": "Location?identifier=https://github.com/synthetichealth/synthea|172ca829-44df-36fa-b1be-3d5048d1b064",
        "display": "BOSTON HEALTH CARE INC"
      }
    }
    """

if __name__ == '__main__':
    unittest.main()