from fastapi import APIRouter, Query
from .meta import connected_media
from .google_signals import rising_topics
from .storage import save,list_saved
from .ai import analyze_opportunity

router=APIRouter()

@router.get("/instagram/media")
async def instagram_media(limit:int=25): return await connected_media(limit)

@router.get("/google/rising")
async def google_rising(geo:str="IN-TN",language:str="ta"): return await rising_topics(geo,language)

@router.post("/opportunities/save")
async def save_opportunity(payload:dict):
    return {"id":save(payload.get("topic","Untitled"),payload.get("platform","unknown"),payload)}

@router.get("/opportunities/saved")
def saved(): return {"items":list_saved()}

@router.post("/ai/analyze")
async def analyze(payload:dict):
    return await analyze_opportunity(payload.get("topic",""),payload.get("evidence",[]))
