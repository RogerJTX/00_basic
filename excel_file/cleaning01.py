import pymongo

client = pymongo.MongoClient('xxx', 1)
db1 = client.xxx
col1 = db1.xxx

num_delete = 0
for num1, i in enumerate(col1.find({},{"html":0})):

    try:

        if num1+1 < 1017:
            continue
        tag = i['tag']
        map = {}
        map['organization'] = i['organization']
        for num2, i2 in enumerate(tag):
            if num2 == 0:
                map['type'] = i2
            # elif num2 == 1:
            #     map['type'] = i2

        print(map, str(num1+1))

        myquery = {"title": i["title"], "publish_time":i["publish_time"]}
        newvalues = {"$set": {"tag": map}}
        col1.update_one(myquery, newvalues)
    except:
        # col1.delete_one({"title": i["title"], "publish_time":i["publish_time"]})
        num_delete+=1
        print("num_delete:", num_delete)