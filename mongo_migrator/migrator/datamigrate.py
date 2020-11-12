from pymongo import MongoClient
import time

class migrator:

  def __init__(self):
    self._status = None
  

  def migrate(self):
    client = MongoClient(host='34.227.105.4:27017',serverSelectionTimeoutMS = 3000)
    mydb = client["mydb"]
    aircol = mydb["airlines"]
    doccount = aircol.count_documents({})
    
    for x in range(0,doccount):
      if x==0:
          data = aircol.find().limit(1)
      else:
          data = aircol.find({'_id': {'$gt': last_id}}).limit(1)
      last_id = data[0]['_id']
      count = x+1
      process = round((count/doccount)*100)
      print(process)
      

