import requests

# alternatives.json
ALT_MAIN_API = 'https://job.firstvds.ru/alternatives.json?'

def get_html(url):
    return requests.get(url)

def alternatives_json(url_address):
    """Правильно считывает json файл"""
    import ast
    alt_json_data = get_html(url_address)

    if alt_json_data:
        alt_json_data = alt_json_data.text
        return  ast.literal_eval(alt_json_data)
    else:
        return None

if __name__ == '__main__':
    x = alternatives_json(ALT_MAIN_API)
    for supply in x['alternatives']:
        print(supply, '=>')
        for alter in x['alternatives'][supply]:
            print(alter)
        print()    
    


