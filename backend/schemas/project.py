from pydantic import BaseModel, ConfigDict


class ProjectBase(BaseModel):
    name: str
    dev_url: str
    test_url: str
    prod_url: str

    model_config = ConfigDict(from_attributes=True)
