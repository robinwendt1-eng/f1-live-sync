import json
import requests
from datetime import datetime

url = "https://api.jolpi.ca/ergast/f1/current/last/results.json"

response = requests.get(url)
data = response.json()

race = data["MRData"]["RaceTable"]["Races"][0]
results = race["Results"]

positions = []

for r in results:
    positions.append({
        "position": r["position"],
        "driver": r["Driver"]["code"]
    })

output = {
    "timestamp": datetime.utcnow().isoformat(),
    "race": race["raceName"],
    "positions": positions
}

with open("output.json", "w") as f:
    json.dump(output, f, indent=2)

print("F1 Daten geladen")
