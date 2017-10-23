import urllib
import requests
# spares.json
MAIN_API = 'https://job.firstvds.ru/spares.json?'



def spares_json(json_api):
    json_data = requests.get(json_api).json() 
    if json_data:
        return json_data
    else:
        return None


if __name__=='__main__':
    
    while True:
        address = input('Address or type "q" to exit: ').upper() # request object
        if address.lower() in ['quit', 'q', 'exit' ]: break # выход из цикла

        url = MAIN_API + urllib.parse.urlencode({'address': address})
        json_data = requests.get(url).json() 

        print(url + '\n')
        if address in json_data:
            for data in json_data[address]:
                print(data + ':', json_data[address][data])
        else: 
            print('invalid request')
        print()
            
