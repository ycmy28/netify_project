from fastapi import FastAPI, Query
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/current_date")
def get_current_date(timezone: str = Query(default="Asia/Jakarta")):
    try:
        local_tz = pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        return {"error": "Invalid timezone"}

    current_date = datetime.now(local_tz).strftime('%Y-%m-%d')
    return {"current_date": current_date}
