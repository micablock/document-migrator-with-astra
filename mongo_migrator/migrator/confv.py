import configparser
import io

class confs:
  
  def confval():
    config = configparser.ConfigParser()
    config.read("/Users/davidjoy/Desktop/terraform-project/stargate_mongo_migrator/mongo-migrator/stargate_mongo_migrator/config.ini")
    #mongo info
    mongohost = config['mongo']['host']
    mongoport = config['mongo']['port']
    #astra info
    clusterid = config['astra']['clusterid']
    region = config['astra']['region']
    username = config['astra']['username']
    password = config['astra']['password']
    collection = config['astra']['collection']
    namespace = config['astra']['namespace']    
    return {'mongohost':mongohost,'mongoport':mongoport,'clusterid':clusterid,'region':region,'username':username,'password':password,'collection':collection,'namespace':namespace}
