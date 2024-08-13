import json
from datetime import datetime
import pytz

def handler(event, context):
    timezone = event.get('queryStringParameters', {}).get('timezone', 'Asia/Jakarta')

    try:
        local_tz = pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid timezone"})
        }

    current_date = datetime.now(local_tz).strftime('%Y-%m-%d')
    return {
        "statusCode": 200,
        "body": json.dumps({"current_date": current_date})
    }
