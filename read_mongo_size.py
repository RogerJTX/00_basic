import pymongo
import bson

client = pymongo.MongoClient('xxx', 0)
# res = db['log'].find_one({"sid": test_id})
db1 = client.xxx
col = db1.xxx
res = col.find_one({'url':'http://www.sv360.cn/a/fuwu/xinwenzhongxin/20180510/45.html'})
print(res)
print(len(bson.BSON.encode(res))) # B
print(len(bson.BSON.encode(res))*1.0/1024/1024) # MB
print(len(bson.BSON.encode(res))*1.0/1024/1024/1024)



print(col.find().count())
print(2.2312626242637634e-05*220000)

col2 = db1.company_auto_news_and_products_maintenance_table
for num, i in enumerate(col2.find()):
    print(num+1)
    myquery = {"website": i['website']}
    newvalues = {"$set": {"size": ''}}

    col2.update_one(myquery, newvalues)