import time
import json
import subprocess
now = time.time()
status = json.load(open("/home/leo/Scripts/protonVPN/data.json"))

if now-status["metadata"]["last_update"] > 60:
    status["metadata"]["last_update"] = now
    status["metadata"]["last_update_readable"] = f"{time.asctime(time.localtime(now))}"
    status_raw = str(subprocess.check_output(['protonvpn', 'status'])).lstrip("b'").rstrip("'").replace(" ", "").split(r"\n")
    status_raw.pop()
    status["metadata"]["request_counter"] += 1
    for s in status_raw:
        tmp = s.split(":", 1)
        status["data"][tmp[0]] = tmp[1]
    json.dump(status, open("/home/leo/Scripts/protonVPN/data.json", "w"), indent=2)
