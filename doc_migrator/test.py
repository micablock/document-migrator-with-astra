from mongo_migrator.migrator.confv import confs

conf = confs.confval()
print(conf['mongohost']+':'+conf['mongoport'])