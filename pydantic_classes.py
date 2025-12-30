from pydantic import BaseModel, Field
from typing import List

class PaperCard(BaseModel):
    paper_title : str  = Field(...,description="Title of the paper")
    paper_summary : str  = Field(...,description="Summary of the paper")
    relevance : str = Field(...,description="The relevance of the paper")
    related_topics : List[str] = Field(...,description="List of related topics")
    