from typing import List, Optional
from pydantic import BaseModel, validator


class ErrorListMessage(BaseModel):
    message: str
    class Config:
        extra = 'allow'
    
class ErrorResponse(BaseModel):
    code: Optional[int] = None
    type: str
    message: Optional[str] = None
    errors: Optional[List[ErrorListMessage]] = None
    
    @validator('errors', pre=True, always=True)
    def require_messge_or_errors(cls, v, values):
        ''' 
        Check to ensure either message or errors is set.
        
        V has the value of errors and values has all the fields validated before errors.
        '''
        if 'message' not in values and not v:
            raise ValueError('Either message or errors is required.')
        return v
    
    @validator('message')
    def pretty_errors(cls, value):
        return value.replace('\n', "")

