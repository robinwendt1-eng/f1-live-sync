import json
from datetime import datetime

data = {
    "timestamp": datetime.utcnow().isoformat(),
    "status": "ok"
}

with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

print("fertig")
