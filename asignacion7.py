import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
payload=response.json()
pprint(payload)
headers = {
           'X-Auth-Token' : payload.get('Token')
          }
response = requests.get("https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device",headers=headers)
payload2=response.json()
pprint(payload2)

payload3=payload2.get('response')

for org in payload3:
    List.append(dict(family=org.get('family'), hostname=org.get('hostname'),
     managementIpAddress=org.get('managementIpAddress'),
      lastUpdated=org.get('lastUpdated'), reachabilityStatus=org.get('reachabilityStatus')))
pprint(List)

