from typing import TypedDict, List

class ReSearchAgentState(TypedDict):
    query:str
    search_results:List[dict]
    web_pages:List[dict]
    notes:List[dict]
    report:str
