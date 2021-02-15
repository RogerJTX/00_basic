import pymongo

client = pymongo.MongoClient('xxx', 1)
db = client.xxx
col1 = db.xxx
col2 = db.xxx


a = '章伟	高诚	'
list_a = a.split('\t')
print(list_a)
print(len(list_a))