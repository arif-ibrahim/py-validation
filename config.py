import json

# load db in json format
# open('db_config.json')
# print("json file opened")
# print("isd")
json_file = "/home/abra/Dev/gaze/repository/py-validation/db_config.json"
config = json.load(open(json_file))
print("ok")
