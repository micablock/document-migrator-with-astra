from celery import shared_task
from celery_progress.backend import ProgressRecorder
from time import sleep
from pymongo import MongoClient
import uuid
import requests
import json
from pprint import pprint
from mongo_migrator.migrator.authenticator import auth
from mongo_migrator.migrator.confv import confs


@shared_task(bind=True)

def go_to_sleep(self,params):
  progress_recorder = ProgressRecorder(self)
  duration = params['duration']
  colname = params['colname']
  mongodbname = params['mongodbname']
  conf = confs.confval()
  host = conf['mongohost']+':'+conf['mongoport']
  client = MongoClient(host=host,serverSelectionTimeoutMS = 3000)
  mydb = client[mongodbname]
  aircol = mydb[colname]
  doccount = aircol.count_documents({})

  token = auth.authenticate()
  # astra migrate
  headers = {
    "x-cassandra-token": str(token),
    "content-type": "application/json"
  }
  
  CLUSTERID = conf['clusterid']
  REGION = conf['region']
  COLLECTION = conf['collection']
  NAMESPACE = conf['namespace']
  URL = f"https://{CLUSTERID}-{REGION}.apps.astra.datastax.com"

  for i in range(doccount):
    sleep(.25)
    if i==0:
      for data in aircol.find().limit(1):
        print(data)
        last_id=data.pop('_id')
        AIRLINE_ID = str(uuid.uuid4())
        print(AIRLINE_ID)
        DOC_ROOT_PATH = f"/api/rest/v2/namespaces/{NAMESPACE}/collections/{COLLECTION}/{AIRLINE_ID}"
        PUTTURL = URL+DOC_ROOT_PATH
        response = requests.request("PUT", PUTTURL, data=json.dumps(data), headers=headers)
        pprint(response.text)
    else:
      for data in aircol.find({'_id': {'$gt': last_id}}).limit(1):
        print(data)
        last_id=data.pop('_id')
        AIRLINE_ID = str(uuid.uuid4())
        DOC_ROOT_PATH = f"/api/rest/v2/namespaces/{NAMESPACE}/collections/{COLLECTION}/{AIRLINE_ID}"
        PUTTURL = URL+DOC_ROOT_PATH
        response = requests.request("PUT", PUTTURL, data=json.dumps(data), headers=headers)
        pprint(response.text)
    progress_recorder.set_progress(i+1,doccount)

  return 'All Documents Processed !! '

