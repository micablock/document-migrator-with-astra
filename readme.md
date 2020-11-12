## Document Migrator Application for Astra

This application helps to migrate documents out of Document based databases to DataStax Astra. This example application uses mongoDB as source of documents that are migrated to Astra using this application.

## Application Flow
1. Home page to connect to mongodb databses
![](images/home.png)

2. Click datbase to identify collections to migrate 
![](images/clickConnect.png)

3. Click collection to migrate data
![](images/Click-Documents.png)

4. Migration Status page
![](images/MigrationStatus.png)


## High Level Architecture 
Key components 
- Document Database : MongoDB
- Application : Django, celery, redis 
- Stargate document API
- DataStax Astra 

![](images/MongoMigratorArchitecturefinal.png)

## Configuration 

All configurations to be setup within `config.ini`

```
[mongo]
host=34.227.105.4
port=27017

[astra]
clusterid=Astra Cluster ID
region=Astra Cluster Region
username=Astra Database Name
password=Astra Database Password
collection=Astra Table name 
namespace=Astra Keyspace Name