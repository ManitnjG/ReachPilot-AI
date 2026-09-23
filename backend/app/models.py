from pydantic import BaseModel
from typing import Optional

class TrendSignal(BaseModel):
    platform:str
    source:str
    topic:str
    geography:str="IN"
    language:str="ta"
    velocity:float=0
    opportunity_score:float=0
    stage:str="Early"
    confidence:str="medium"
    evidence_url:Optional[str]=None
