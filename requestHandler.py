import httpx
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()


def getUserStatsForGame():
    params = {'appid': os.getenv('APP_ID'), 'steamid': os.getenv('STEAM_ID')}
    headers = {'x-webapi-key': os.getenv('DEV_KEY')}

    response = httpx.get(os.getenv('URL'), params=params, headers=headers)

    code = response.status_code
    print("[RequestHandler][getUserStatsForGame] URL: " + str(response.url))
    print("[RequestHandler][getUserStatsForGame] Statuscode: " + str(code))
    if code == 200:
        return response.text
    else:
        return None
