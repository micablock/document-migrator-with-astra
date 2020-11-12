from pymongo import MongoClient

class MongoConnect:

  def dblist():
    client = MongoClient(host='34.227.105.4:27017',serverSelectionTimeoutMS = 3000)
    dblist = client.list_database_names()
    return dblist

  def dbcollist(dbname):
    client = MongoClient(host='34.227.105.4:27017',serverSelectionTimeoutMS = 3000)
    mydb = client[dbname]
    dbcol = mydb.list_collection_names()
    return dbcol
  
  def count(dbname,colname):
    client = MongoClient(host='34.227.105.4:27017',serverSelectionTimeoutMS = 3000)
    mydb = client[dbname]
    aircol = mydb[colname]
    doccount = aircol.count_documents({})
    return doccount