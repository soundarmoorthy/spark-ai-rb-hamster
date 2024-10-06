

import unittest
import json

from fhirclient.models.procedure import Procedure
from marshmallow.fields import String

from src.resource_mapper import ResourceMapper

# Use fhirclient. Write a test to check if the below data() for a
# procedure resource can be loaded as a FHIR resource using fhirclient.

class TestProcedure(unittest.TestCase):
    def test_procedure(self):
        resource = json.loads(data())

        # Use resourceMapper to map the resource to a FHIR resource
        resource_type, obj = ResourceMapper.map(resource)

        # Assert the object is not null
        self.assertIsNotNone(obj)

        # Assert the object is of type Procedure
        self.assertEqual(resource_type, 'Procedure')

        # Assert code.coding.code is 710824005
        self.assertEqual(obj.code.coding[0].code, '710824005')

if __name__ == '__main__':
    unittest.main()

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