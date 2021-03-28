import json

print(round(json.load(open("/home/leo/Scripts/conky/data.json"))["request_result"]["data"]["03403"]["weekIncidence"], 2))