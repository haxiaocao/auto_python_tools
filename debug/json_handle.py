# https://martin-thoma.com/configuration-files-in-python/
import json

# get the json file data
with open('json_config.json') as json_data_file:
    data=json.load(json_data_file)
print data


# save data into json file
with open('json_config.json','w') as outfile:
    json.dump(data,outfile)
