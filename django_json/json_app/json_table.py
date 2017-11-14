from .spares_json import MAIN_API, spares_json
from .alternatives_json import ALT_MAIN_API, alternatives_json


alt = alternatives_json(ALT_MAIN_API)
spare = spares_json(MAIN_API)

task_dict = {}

for key in alt['alternatives']:
    task_dict.setdefault(key,{})
    for item in alt['alternatives'][key]:
        for skey in spare:
            if item.upper() == skey.upper():
                for key_par, value in spare[skey].items():
                    task_dict[key].setdefault(key_par,[]).append(value)

for key in task_dict:
    task_dict[key]['count'] = sum(task_dict[key]['count'])
    task_dict[key]['arrive'] = sum(task_dict[key]['arrive'])
    task_dict[key]['mustbe'] = sum(task_dict[key]['mustbe'])
    


