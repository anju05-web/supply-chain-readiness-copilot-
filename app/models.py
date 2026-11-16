from pydantic import BaseModel, Field
from typing import Optional

class WorkOrderCreate(BaseModel):
    equipment_id: str = Field(..., example="GEN-04")
    fault_code: Optional[str] = Field(None, example="E12")
    issue_description: str = Field(..., example="Overheating after 2 hours of load")

class WorkOrderResponse(WorkOrderCreate):
    id: int
    status: str
