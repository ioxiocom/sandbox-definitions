from pydantic import Field

from src.converter import CamelCaseModel, DataProductDefinition


class BasicCompanyInfoRequest(CamelCaseModel):
    company_id: str = Field(
        ...,
        title="Company ID",
        description="The ID of the company",
        example="2464491-9",
    )


class BasicCompanyInfoResponse(CamelCaseModel):
    name: str = Field(
        ..., title="Name of the company", example="Digital Living International Oy"
    )
    company_id: str = Field(..., title="ID of the company", example="2464491-9")
    company_form: str = Field(
        ..., title="The company form of the company", example="LLC"
    )
    registration_date: str = Field(
        ..., title="Date of registration for the company", example="2012-02-23"
    )


DEFINITION = DataProductDefinition(
    description="Data Product for basic company info",
    request=BasicCompanyInfoRequest,
    response=BasicCompanyInfoResponse,
    route_description="Information about the company",
    summary="Basic Company Info",
)
