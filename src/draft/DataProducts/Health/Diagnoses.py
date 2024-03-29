from typing import List

from pydantic import Field

from src.converter import CamelCaseModel, DataProductDefinition


class HealthDiagnosesRequest(CamelCaseModel):
    pass


class HealthDiagnosesResponse(CamelCaseModel):
    diagnoses: List[str] = Field(
        ..., description="List of users diagnoses in ICD10 code", example=["icd10:J45"]
    )


DEFINITION = DataProductDefinition(
    description="Data Product for user's diagnoses with ICD10 codes",
    request=HealthDiagnosesRequest,
    response=HealthDiagnosesResponse,
    route_description="Health diagnoses in ICD codes",
    summary="Persons Diagnoses",
)
