from pymongo import MongoClient
from mongo_migrator.migrator.confv import confs

class MongoConnect:

  def dblist():
    conf = confs.confval()
    host = conf['mongohost']+':'+conf['mongoport']
    client = MongoClient(host=host,serverSelectionTimeoutMS = 3000)
    dblist = client.list_database_names()
    return dblist

  def dbcollist(dbname):
    conf = confs.confval()
    host = conf['mongohost']+':'+conf['mongoport']
    client = MongoClient(host=host,serverSelectionTimeoutMS = 3000)
    mydb = client[dbname]
    dbcol = mydb.list_collection_names()
    return dbcol
  
  def count(dbname,colname):
    conf = confs.confval()
    host = conf['mongohost']+':'+conf['mongoport']
    client = MongoClient(host=host,serverSelectionTimeoutMS = 3000)
    mydb = client[dbname]
    aircol = mydb[colname]
    doccount = aircol.count_documents({})
    return doccount