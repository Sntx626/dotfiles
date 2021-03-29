import os
import datetime
import json

def finalize() -> None:
    data = json.load(open("/home/leo/Scripts/update/data.json"))
    if data["managed_snapshot"] is None:
        print("No snapshot in data.json present!")
        return
    most_recent_snapshot_name = data["managed_snapshot"]
    os.system(f"echo finalized snapshot {most_recent_snapshot_name}")
    data["managed_snapshot"] = None
    print("Finalized snapshot:", most_recent_snapshot_name)
    json.dump(data, open("/home/leo/Scripts/update/data.json", "w"), indent=2)

def rollback() -> None:
    data = json.load(open("/home/leo/Scripts/update/data.json"))
    if data["managed_snapshot"] is None:
        print("No snapshot in data.json present!")
        return
    most_recent_snapshot_name = data["managed_snapshot"]
    os.system(f"echo tolling back to this snapshot {most_recent_snapshot_name}")
    data["managed_snapshot"] = None
    print("Rolled back to snapshot:", most_recent_snapshot_name)
    json.dump(data, open("/home/leo/Scripts/update/data.json", "w"), indent=2)

def take_snapshot() -> None:
    data = json.load(open("/home/leo/Scripts/update/data.json"))
    if not data["managed_snapshot"] is None:
        print("Snapshot in data.json present!")
        return
    now = datetime.datetime.now()
    most_recent_snapshot_name = f"root_snapshot_{now.year}-{now.month}-{now.day}_{now.hour}{now.minute}"
    os.system(f"echo taking snapshot {most_recent_snapshot_name}")
    data["managed_snapshot"] = most_recent_snapshot_name
    print("Took snapshot:", most_recent_snapshot_name)
    json.dump(data, open("/home/leo/Scripts/update/data.json", "w"), indent=2)