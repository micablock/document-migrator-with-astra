import requests
import json

class auth:

    def authenticate():
      url = "https://c72c60e1-d1c1-4730-8d6a-413abce921ff-us-east-1.apps.astra.datastax.com/api/rest/v1/auth"
      payload = {
                      "username": "mongo_migrator",
                      "password": "mongo_migrator"
                   }
      headers = {
                      "accept": "*/*",
                      "x-cassandra-request-id": "134",
                      "content-type": "application/json"
                   }
      response = requests.request("POST", url, json=payload, headers=headers)
      token = json.loads(response.text)['authToken']
      return token