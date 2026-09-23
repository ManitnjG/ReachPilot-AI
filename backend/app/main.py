import os
from typing import Optional
import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(title="ReachPilot AI API",version="0.2.0")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

YT="https://www.googleapis.com/youtube/v3"

@app.get("/health")
def health():
    return {"ok":True,"service":"reachpilot-api"}

@app.get("/sources")
def sources():
    return {
      "youtube":{"status":"configured" if os.getenv("YOUTUBE_API_KEY") else "needs_key","type":"official_api"},
      "instagram":{"status":"needs_meta_auth","type":"authorized_meta_api","note":"Connected-account/authorized coverage only; do not claim complete public Reel coverage."},
      "google_trends":{"status":"planned","type":"official_or_licensed_signal"},
      "ai":{"status":"configured" if os.getenv("AI_API_KEY") else "needs_key","type":"server_side"}
    }

@app.get("/youtube/search")
async def youtube_search(q:str=Query(...,min_length=2),region:str="IN",language:str="ta",max_results:int=20):
    key=os.getenv("YOUTUBE_API_KEY")
    if not key: raise HTTPException(503,"YOUTUBE_API_KEY is not configured on the backend")
    max_results=max(1,min(max_results,50))
    params={"part":"snippet","q":q,"type":"video","order":"date","regionCode":region,"relevanceLanguage":language,"maxResults":max_results,"key":key}
    async with httpx.AsyncClient(timeout=20) as c:
        sr=(await c.get(f"{YT}/search",params=params)).json()
        if "error" in sr: raise HTTPException(502,sr["error"].get("message","YouTube API error"))
        ids=[x["id"]["videoId"] for x in sr.get("items",[]) if x.get("id",{}).get("videoId")]
        stats={}
        if ids:
            vr=(await c.get(f"{YT}/videos",params={"part":"statistics,contentDetails","id":",".join(ids),"key":key})).json()
            stats={x["id"]:x for x in vr.get("items",[])}
    out=[]
    for x in sr.get("items",[]):
        vid=x.get("id",{}).get("videoId")
        if not vid: continue
        sn=x["snippet"]; st=stats.get(vid,{})
        out.append({"id":vid,"title":sn.get("title"),"channel":sn.get("channelTitle"),"published_at":sn.get("publishedAt"),"thumbnail":sn.get("thumbnails",{}).get("high",{}).get("url"),"statistics":st.get("statistics",{}),"duration":st.get("contentDetails",{}).get("duration"),"url":f"https://www.youtube.com/watch?v={vid}"})
    return {"platform":"youtube","query":q,"region":region,"language":language,"items":out}

@app.get("/youtube/popular")
async def youtube_popular(region:str="IN",max_results:int=25):
    key=os.getenv("YOUTUBE_API_KEY")
    if not key: raise HTTPException(503,"YOUTUBE_API_KEY is not configured on the backend")
    params={"part":"snippet,statistics,contentDetails","chart":"mostPopular","regionCode":region,"maxResults":max(1,min(max_results,50)),"key":key}
    async with httpx.AsyncClient(timeout=20) as c:
        data=(await c.get(f"{YT}/videos",params=params)).json()
    if "error" in data: raise HTTPException(502,data["error"].get("message","YouTube API error"))
    return {"platform":"youtube","region":region,"items":data.get("items",[])}

@app.get("/instagram/status")
def instagram_status():
    return {"platform":"instagram","connected":bool(os.getenv("META_ACCESS_TOKEN")),"coverage":"authorized Meta API only","message":"Meta credentials and user authorization are required before account insights/media can be returned."}
