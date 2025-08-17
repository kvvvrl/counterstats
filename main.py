
import json
import dbHandler
import requestHandler
import hashlib

text = requestHandler.getUserStatsForGame()
response_json = json.loads(text)
stats = response_json['playerstats']['stats']
encoded = str(stats).encode()
hashed = hashlib.md5(encoded).hexdigest()
db = dbHandler.DBHandler()
db.save_pickup(str(stats), hashed)
