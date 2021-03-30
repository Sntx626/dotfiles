import os
import datetime
import json

def finalize() -> None:
    data = json.load(open("/home/leo/Scripts/update/data.json"))
    if data["managed_snapshot"] is None:
        print("No snapshot in data.json present!")
        return
    most_recent_snapshot_name = data["managed_snapshot"]
    os.system(f"sudo lvremove /dev/volgroup0/{most_recent_snapshot_name}")
    data["managed_snapshot"] = None
    print("Executed: finalize snapshot for", most_recent_snapshot_name)
    json.dump(data, open("/home/leo/Scripts/update/data.json", "w"), indent=2)

def rollback() -> None:
    data = json.load(open("/home/leo/Scripts/update/data.json"))
    if data["managed_snapshot"] is None:
        print("No snapshot in data.json present!")
        return
    most_recent_snapshot_name = data["managed_snapshot"]
    os.system(f"lvconvert --merge /dev/volgroup0/{most_recent_snapshot_name}")
    data["managed_snapshot"] = None
    print("Executed: rollback to snapshot with", most_recent_snapshot_name)
    json.dump(data, open("/home/leo/Scripts/update/data.json", "w"), indent=2)

def take_snapshot() -> None:
    data = json.load(open("/home/leo/Scripts/update/data.json"))
    if not data["managed_snapshot"] is None:
        print(f"Snapshot `{data['managed_snapshot']}` in data.json present!")
        return
    now = datetime.datetime.now()
    most_recent_snapshot_name = f"root_snapshot_{now.year}-{now.month}-{now.day}_{str(now.hour).zfill(2)}{str(now.minute).zfill(2)}"
    os.system(f"sudo lvcreate -L 64GB -s -n {most_recent_snapshot_name} /dev/mapper/volgroup0-lv_root")
    data["managed_snapshot"] = most_recent_snapshot_name
    print("Executed: take snapshot with", most_recent_snapshot_name)
    json.dump(data, open("/home/leo/Scripts/update/data.json", "w"), indent=2)

def ask(question:str, responses:list, use_newline:bool=True) -> int:
    question_with_select = question + "\n"
    for i in range(len(responses)):
        responses[i] = str(responses[i])
        question_with_select += f"\n{i+1}. {responses[i]}"
    question_with_select += "\n\nSelection: "

    if use_newline:
        answer = str(input(question_with_select))
    else:
        answer = str(input(question_with_select))

    selection = []
    for i in range(1, len(responses)+1):
        selection.append(str(i))
    
    if answer in selection:
        return selection.index(answer)
    else:
        print(f"Please answer using only {list(range(1, len(responses)+1))}!")
        return ask(question=question, responses=responses, use_newline=use_newline)

def main() -> None:
    selection = ask("Do you want to:", responses=["Show info?", "Take a Snapshot?", "Finalize a Snapshot?", "Rollback to a Snapshot?", "Cancel?"], use_newline=False)
    print("")
    if selection == 0:
        os.system("sudo lvs")
    elif selection == 1:
        take_snapshot()
    elif selection == 2:
        finalize()
    elif selection == 3:
        rollback()
    elif selection == 4:
        print("Aborted!")
        return
    print("\ndone!")

if __name__ == "__main__":
    main()