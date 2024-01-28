from pydantic import BaseModel
from typing import List


class AdRequest(BaseModel):
    adIdList: List[int]

class AdResponse(BaseModel):
    adId: int
    estimatedCVR: float
