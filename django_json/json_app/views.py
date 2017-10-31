from .alternatives_json import ALT_MAIN_API, alternatives_json
from .spares_json import MAIN_API, spares_json
from django.shortcuts import render
from .json_table import task_dict
from django.http import HttpResponse
import json


def show_spares_json(request): 
    data = spares_json(MAIN_API)
    args={}
    args['data'] = data
    return render(request, 'spare_table.html', args)

def show_alt_json(request):
    alt_data = alternatives_json(ALT_MAIN_API)
    args = {}
    args['alt_data'] = alt_data['alternatives']
    return render(request, 'alt_table.html',args)

def show_json(request):
    json_data = {}
    for key in task_dict:
        if task_dict[key]['count'] + task_dict[key]['arrive'] > task_dict[key]['mustbe']:
            json_data.setdefault(key, task_dict[key])

    json_data = json.dumps(json_data)

    return HttpResponse( json_data)
    
def show_json_table(request):
    json_table = task_dict
    json_data = {}
    args = {}
    args['json_table'] = json_table  

    for key in task_dict:
        if task_dict[key]['count'] + task_dict[key]['arrive'] > task_dict[key]['mustbe']:
            json_data.setdefault(key, task_dict[key])
            
    args['json_data'] = json_data
    return render(request, 'json_table.html',args)
