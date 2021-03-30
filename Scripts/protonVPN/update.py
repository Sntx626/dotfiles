import json
import subprocess
import time

now = time.time()
status = json.load(open("/home/leo/Scripts/protonVPN/data.json"))

if now-status["last_update"] > 300:
    status["last_update"] = now
    status["last_update_readable"] = f"{time.asctime(time.localtime(now))}"
    status_raw = str(subprocess.check_output(['protonvpn', 'status'])).lstrip("b'").rstrip("'").split(r"\n")
    status_raw.pop()
    status["request_counter"] += 1
    for s in status_raw:
        tmp = s.split(":", 1)
        tmp[0] = str(tmp[0]).replace(' ', '_')
        if tmp[0] in ["Sent", "Received"]: # ie.: tmp[1] == 529.86 KB
            subdata = tmp[1].strip(" ").split(" ")
            print("subdata", subdata)
            print("pre round", float(subdata[0]), type(float(subdata[0])))
            print("past round", round(float(subdata[0]), 2))
            tmp[1] == f"{round(float(subdata[0]), 2)} {subdata[1]}"
            print("tmp[1]", tmp[1])
        with open(f"/home/leo/Scripts/protonVPN/{tmp[0]}.txt", "w") as f:
            f.write(tmp[1].strip(" "))
    json.dump(status, open("/home/leo/Scripts/protonVPN/data.json", "w"), indent=2)
else:
    with open("/home/leo/Scripts/protonVPN/next_update_in.txt", "w") as f:
        f.write(f"{300-int(now-status['last_update'])}".zfill(2))