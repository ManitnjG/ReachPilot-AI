# Adapter boundary for licensed/authorized Google trend/search signals.
# We intentionally do not fabricate Google Trends data.
async def rising_topics(geo:str="IN-TN", language:str="ta"):
    return {"configured":False,"geo":geo,"language":language,"items":[],
            "message":"Google trend signal provider is not configured yet."}
