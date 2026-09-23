import os, httpx

async def analyze_opportunity(topic:str, evidence:list[dict]):
    key=os.getenv("AI_API_KEY"); base=os.getenv("AI_BASE_URL"); model=os.getenv("AI_MODEL")
    if not (key and base and model):
        return {"available":False,"summary":"AI is not configured. Source evidence remains available.","angles":[]}
    prompt=("You are ReachPilot AI. Analyze only the supplied evidence. Never invent trend facts. "
            "Return concise creator opportunities, original angles, hook ideas and risks. Topic: "+topic+
            "\nEvidence: "+str(evidence[:20]))
    async with httpx.AsyncClient(timeout=35) as c:
        r=await c.post(base.rstrip("/")+"/chat/completions",headers={"Authorization":"Bearer "+key},
            json={"model":model,"messages":[{"role":"user","content":prompt}],"temperature":0.4})
        r.raise_for_status(); data=r.json()
    return {"available":True,"text":data["choices"][0]["message"]["content"]}
