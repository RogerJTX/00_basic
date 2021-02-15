import pymongo
from random import random, randint


client = pymongo.MongoClient('xxx', 1)
client.admin.authenticate("xxx", "xxx")
db1 = client.xxx
col1 = db1.xxx
col2 = db1.xxx
from tqdm import tqdm

count_mongo = col1.find().count()
print(count_mongo)

print(random())

pbar = tqdm(col1.find())
for num, i in enumerate(pbar):
    # print(num)
    pbar.set_description("Processing %s" % i['name'])
    # pbar.set_postfix(loss=random(), gen=randint(1, 999), str="h", lst=[1, 2])
    pbar.set_postfix(Processing=str(num+1)+'/'+str(count_mongo))
