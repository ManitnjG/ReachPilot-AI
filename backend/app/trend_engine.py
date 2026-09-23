from datetime import datetime, timezone
from math import log10

def engagement_velocity(views:int, likes:int, comments:int, published_at:str):
    try:
        dt=datetime.fromisoformat(published_at.replace("Z","+00:00"))
        hours=max((datetime.now(timezone.utc)-dt).total_seconds()/3600,1)
    except Exception:
        hours=24
    weighted=views + likes*8 + comments*20
    return round(weighted/hours,2)

def opportunity_score(velocity:float, views:int, freshness_hours:float=24):
    velocity_score=min(50, max(0, log10(max(velocity,1))*12))
    reach_score=min(25, max(0, log10(max(views,1))*4))
    freshness=max(0,25-min(freshness_hours,72)/72*25)
    return round(min(100,velocity_score+reach_score+freshness),1)

def stage(score:float):
    if score>=80:return "Peak"
    if score>=60:return "Rising"
    if score>=35:return "Early"
    return "Cooling"
