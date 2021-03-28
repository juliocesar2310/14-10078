import requests
from pprint import pprint
import time
import simplejson as json

while True:
    response = requests.post(
        'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
        headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
    response.raise_for_status()
    payload=response.json()
    headers = {
               'X-Auth-Token' : payload.get('Token')
              }
    response = requests.get("https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device",headers=headers)
    payload2=response.json()


    payload3=payload2.get('response')

    List = []
    for org in payload3:
        List.append(dict(hostname=org.get('hostname'),reachabilityStatus=org.get('reachabilityStatus')))

    with open ('json8.json','w') as f:
        json.dump(List,f)
    pprint("Json Actualizado. Proxima en: 5 minutos")
    time.sleep(300)
