# https://automatetheboringstuff.com/chapter14/
import json

# read json with Load(s) method , and the return value is Python dictionary data structure.
#load for File, and loads for string ;
def read_json():
    str_json='{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
    json_data_python=json.loads(str_json)
    # json_data_python=json.load(filename)
    print json_data_python


def write_json():
    python_value={'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
    # json.dumps(obj,filename)
    str_jsons=json.dumps(python_value)
    print str_jsons

# read_json()
write_json()
