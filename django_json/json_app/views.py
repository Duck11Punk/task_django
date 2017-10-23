from django.shortcuts import render
from .spares_json import spares_json, MAIN_API
from .alternatives_json import alternatives_json, get_html, ALT_MAIN_API
from .json_table import sup2
from .json_dump import dump_json
from django.http import HttpResponse


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
    for key in sup2:
        if sup2[key]['count'] + sup2[key]['arrive'] > sup2[key]['mustbe']:
            json_data.setdefault(key, sup2[key])

    json_data = dump_json(json_data)

    return HttpResponse( json_data)
    
def show_json_table(request):
    json_table = sup2
    json_data = {}
    args = {}
    args['json_table'] = json_table  

    for key in sup2:
        if sup2[key]['count'] + sup2[key]['arrive'] > sup2[key]['mustbe']:
            json_data.setdefault(key, sup2[key])
            
    args['json_data'] = json_data
    return render(request, 'json_table.html',args)
