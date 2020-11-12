import requests
import json
from doc_migrator.migrator.confv import confs

class auth:

    def authenticate(): # Astra Authentication 
       conf = confs.confval()
       CLUSTERID = conf['clusterid']
       REGION = conf['region']
       USERNAME = conf['username']
       PASSWORD = conf['password']
       url = f"https://{CLUSTERID}-{REGION}.apps.astra.datastax.com/api/rest/v1/auth"
       payload = {
                      "username": USERNAME,
                      "password": PASSWORD
                   }
       headers = {
                      "accept": "*/*",
                      "x-cassandra-request-id": "134",
                      "content-type": "application/json"
                   }
       response = requests.request("POST", url, json=payload, headers=headers)
       token = json.loads(response.text)['authToken']
       return token