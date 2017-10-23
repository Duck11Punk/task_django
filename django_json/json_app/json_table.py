from .alternatives_json import ALT_MAIN_API, alternatives_json
from .spares_json import MAIN_API, spares_json
from collections import defaultdict

alt = alternatives_json(ALT_MAIN_API)
spare = spares_json(MAIN_API)



task_dict = {}
sup={}
support = {}
keys = alt['alternatives'].keys()
alt_picks = alt['alternatives'].values()

for item in alt_picks:
    for supply in item:
        if supply in ['RAM 16Gb PC4-2133']:
            support.update({supply: spare.get('RAM 16Gb PC4-2133 REG')})
            continue
        if supply =='RAM 16Gb PC4-2400':
            support.update({supply: spare.get('RAM 16GB PC4-2400 REG')})
            continue
        support.update({supply: spare.get(supply)})



task_dict = defaultdict(list)

def main(task_dict,support, alt):
    for key_alt in alt['alternatives']: 
        for value_alt in alt['alternatives'][key_alt]:
            task_dict[key_alt].append(support[value_alt]) 
    return task_dict


x = main(task_dict, support, alt)

for item in x:
    sup.setdefault(item, []) 
    for value in x[item]:
        for key, num in value.items():
            sup[item].append({key: value[key]})
        
sup2 = {}

for key, value in sup.items():
    sup2.setdefault(key,{})
    for dic in x[key]:
        for par1 in dic:
            sup2[key].setdefault(par1,[]).append(dic[par1])
            

for key in sup2:
    sup2[key]['count'] = sum(sup2[key]['count'])
    sup2[key]['arrive'] = sum(sup2[key]['arrive'])
    sup2[key]['mustbe'] = sum(sup2[key]['mustbe'])
    











    




