from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic import BaseSettings, Field
from enum import Enum



class Label(Enum):
    POSITIVE='POSITIVE'
    NEGATIVE='NEGATIVE'


class Classification(BaseModel):
    label:Label
    score:float

    class Config:
        use_enum_values = True
