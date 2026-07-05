import json
import requests
from datetime import datetime

url = "https://api.jolpi.ca/ergast/f1/current/last/results.json"
data = requests.get(url).json()

race = data["MRData"]["RaceTable"]["Races"][0]
results = race["Results"]

positions = []

for r in results:
    positions.append({
        "position": int(r["position"]),
        "driver": r["Driver"]["code"],
        "team": r["Constructor"]["name"]
    })

output = {
    "timestamp": datetime.utcnow().isoformat(),
    "race": race["raceName"],
    "round": race["round"],
    "season": race["season"],
    "positions": positions
}

with open("output.json", "w") as f:
    json.dump(output, f, indent=2)

print("F1 LIVE DATA UPDATED")
