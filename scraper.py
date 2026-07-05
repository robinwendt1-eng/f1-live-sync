import json
from datetime import datetime

# Testdaten – werden später durch echte Live-Daten ersetzt
live_data = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "race": "Test",
    "positions": [
        {"position": 1, "driver": "NOR"},
        {"position": 2, "driver": "VER"},
        {"position": 3, "driver": "PIA"},
        {"position": 4, "driver": "RUS"},
        {"position": 5, "driver": "LEC"},
        {"position": 6, "driver": "HAM"},
        {"position": 7, "driver": "ANT"},
        {"position": 8, "driver": "HAD"},
        {"position": 9, "driver": "ALB"},
        {"position": 10, "driver": "SAI"}
    ]
}

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(live_data, f, indent=2)

print("output.json erstellt")
