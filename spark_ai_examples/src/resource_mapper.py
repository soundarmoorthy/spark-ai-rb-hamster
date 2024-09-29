
# Write a class that will map the resourceType to the corresponding resource class
# The class should have a method that will return the resource class for a given resourceType
# The class should have a method that will return the resource class for a given resourceType
from fhirclient.models.observation import Observation
from fhirclient.models.patient import Patient
from fhirclient.models.procedure import Procedure
from fhirclient.models.diagnosticreport import DiagnosticReport
from fhirclient.models.medicationadministration import MedicationAdministration
from fhirclient.models.medicationdispense import MedicationDispense
from fhirclient.models.medicationrequest import MedicationRequest
from fhirclient.models.medicationstatement import MedicationStatement
from fhirclient.models.explanationofbenefit import ExplanationOfBenefit
from fhirclient.models.coverage import Coverage
from fhirclient.models.claimresponse import ClaimResponse
from fhirclient.models.organization import Organization
from fhirclient.models.practitioner import Practitioner
from fhirclient.models.practitionerrole import PractitionerRole
from fhirclient.models.encounter import Encounter
from fhirclient.models.condition import Condition
from fhirclient.models.allergyintolerance import AllergyIntolerance
from fhirclient.models.immunization import Immunization
from fhirclient.models.documentreference import DocumentReference
from fhirclient.models.provenance import Provenance
from fhirclient.models.careplan import CarePlan
from fhirclient.models.medication import Medication
from fhirclient.models.group import Group
from fhirclient.models.device import Device
from fhirclient.models.careteam import CareTeam

from fhirclient.models.claim import Claim

class ResourceMapper:
    def __init__(cls):
        pass

    @classmethod
    def map(cls, resource_json):
        # Decide if strict mode should be enabled
        strict: bool = False
        resource_type = resource_json.get('resourceType')
        if resource_type is None:
            raise ValueError('Resource type not found in resource JSON')

        match resource_type:
            case 'Observation':
                return resource_type, Observation(resource_json, strict=strict)
            case 'Patient':
                return resource_type, Patient(resource_json, strict=strict)
            case 'Procedure':
                return resource_type, Procedure(resource_json, strict=strict)
            case 'DiagnosticReport':
                return resource_type, DiagnosticReport(resource_json, strict=strict)
            case 'MedicationAdministration':
                return resource_type, MedicationAdministration(resource_json, strict=strict)
            case 'MedicationDispense':
                return resource_type, MedicationDispense(resource_json, strict=strict)
            case 'MedicationRequest':
                return resource_type, MedicationRequest(resource_json, strict=strict)
            case 'MedicationStatement':
                return resource_type, MedicationStatement(resource_json, strict=strict)
            case 'Claim':
                return resource_type, Claim(resource_json, strict=strict)
            case 'ExplanationOfBenefit':
                return resource_type, ExplanationOfBenefit(resource_json, strict=strict)
            # Generate case statements for the remaining resource types
            case 'Coverage':
                return resource_type, Coverage(resource_json, strict=strict)
            case 'ClaimResponse':
                return resource_type, ClaimResponse(resource_json, strict=strict)
            case 'Organization':
                return resource_type, Organization(resource_json, strict=strict)
            case 'Practitioner':
                return resource_type, Practitioner(resource_json, strict=strict)
            case 'PractitionerRole':
                return resource_type, PractitionerRole(resource_json, strict=strict)
            case 'Encounter':
                return resource_type, Encounter(resource_json, strict=strict)
            case 'Condition':
                return resource_type, Condition(resource_json, strict=strict)
            case 'AllergyIntolerance':
                return resource_type, AllergyIntolerance(resource_json, strict=strict)
            case 'Immunization':
                return resource_type, Immunization(resource_json, strict=strict)
            case 'DocumentReference':
                return resource_type, DocumentReference(resource_json, strict=strict)
            case 'Provenance':
                return resource_type, Provenance(resource_json, strict=strict)
            case 'CarePlan':
                return resource_type, CarePlan(resource_json, strict=strict)
            case 'Medication':
                return resource_type, Medication(resource_json, strict=strict)
            case 'Group':
                return resource_type, Group(resource_json, strict=strict)
            case 'Device':
                return resource_type, Device(resource_json, strict=strict)
            case 'CareTeam':
                return resource_type, CareTeam(resource_json, strict=strict)
            case _:
                raise ValueError(f'Unsupported resource type: {resource_type}')