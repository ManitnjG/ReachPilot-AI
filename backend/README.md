# ReachPilot backend

## Connected foundation
The backend now has a real official YouTube Data API connector and safe placeholders for Meta/Instagram authorization and AI.

### Configure
Copy .env.example into your deployment environment. Never put production API keys in the Android APK or Git repository.

Required for live YouTube:
- YOUTUBE_API_KEY

Then run:
uvicorn app.main:app --host 0.0.0.0 --port 8000

### Endpoints
- GET /health
- GET /sources
- GET /youtube/search?q=chennai
- GET /youtube/popular?region=IN
- GET /instagram/status

Instagram will only expose data available through Meta-authorized access. ReachPilot will not label third-party web samples as complete Instagram trend data.
