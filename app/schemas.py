from pydantic import BaseModel, EmailStr, Field
from typing import List, Union, Optional
from datetime import date

class IncidentFilter(BaseModel):
    page: Optional[int] = Field(default=2, ge=1)
    limit: Optional[int] = Field(default=10, le=100)
    start_date: Optional[str] = "2025-01-31"
    end_date: Optional[date] = "2025-01-30"
    
    alarm_type_ids: Optional[Union[List[int], int]] = None
    excluded_alarm_type_ids: Optional[Union[List[int], int]] = None
    notification_ids: Optional[Union[List[int], int]] = None
    alarm_ids: Optional[Union[List[int], int]] = None
    
    status: Optional[str] = None
    assignees: Optional[List[EmailStr]] = None
    excluded_assignees: Optional[List[EmailStr]] = None
    excluded_status: Optional[Union[List[str], str]] = None
    
    tags: Optional[Union[List[str], str]] = None
    excluded_tags: Optional[Union[List[str], str]] = None
    
    alarm_main_types: Optional[Union[List[str], str]] = None
    excluded_alarm_main_types: Optional[Union[List[str], str]] = None
    alarm_sub_types: Optional[Union[List[str], str]] = None
    excluded_alarm_sub_types: Optional[Union[List[str], str]] = None
    alarm_title: Optional[Union[List[str], str]] = None
    excluded_alarm_title: Optional[Union[List[str], str]] = None
    
    severities: Optional[str] = None
