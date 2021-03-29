try:
    import time
    import json
    import requests
    now = time.time()
    data = json.load(open("/home/leo/Scripts/conky/data.json"))

    if now-data["last_update"] > 600:
        data["last_update"] = now
        data["last_update_readable"] = f"{time.asctime(time.localtime(now))}"
        r = requests.get(f"https://api.corona-zahlen.org/districts/{data['ags']}")
        if r.ok:
            data["request_result"] = r.json()
        else:
            data["request_result"] = {"data":{"weekInzident":"unknown", "name":"unknown", "state":"unknown"}}
        data["request_counter"] += 1
        json.dump(data, open("/home/leo/Scripts/conky/data.json", "w"), indent=2)
except Exception as e:
    print(e)
