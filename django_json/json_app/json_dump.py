import json
from json2html import *

def dump_json(json_data):
    json_datas = json.dumps(json_data, sort_keys=True)
    json_datas = json2html.convert(json=json_datas)
    return json_datas

