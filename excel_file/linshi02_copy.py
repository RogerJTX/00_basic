import pymongo
import copy
client = pymongo.MongoClient('xxxx', 1)
db = client.xxx
col1 = db.xxx
col2 = db.xxx

for i in col2.find():
    print(i['title'])
    organization = i['search_key']
    myquery = {'title':i['title'], 'publish_time':i['publish_time']}
    newvalues = {"$set":{'tag':['公司']}}
    col2.update_one(myquery, newvalues)
    newvalues = {"$set":{'organization':organization}}
    col2.update_one(myquery, newvalues)

