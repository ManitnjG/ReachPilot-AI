import os, httpx
GRAPH="https://graph.facebook.com/v23.0"

async def connected_media(limit:int=25):
    token=os.getenv("META_ACCESS_TOKEN")
    ig_id=os.getenv("INSTAGRAM_BUSINESS_ACCOUNT_ID")
    if not token or not ig_id:
        return {"connected":False,"items":[],"message":"Meta user authorization and Instagram professional account ID are required."}
    fields="id,caption,media_type,media_product_type,media_url,permalink,timestamp,thumbnail_url"
    async with httpx.AsyncClient(timeout=20) as c:
        r=await c.get(f"{GRAPH}/{ig_id}/media",params={"fields":fields,"limit":min(limit,50),"access_token":token})
        data=r.json()
    if "error" in data:return {"connected":True,"error":data["error"],"items":[]}
    return {"connected":True,"items":data.get("data",[])}
