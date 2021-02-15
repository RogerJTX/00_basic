import pymongo

client = pymongo.MongoClient('xxx', 1)
db1 = client.xxx
col1 = db1.xxx

num_delete = 0
dict_all = {}
with open('manager_revise.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        list_simple_title = line.split('\t')
        if len(list_simple_title)>2:
            list_simple_title_true = list_simple_title[1:]
            key1 = list_simple_title_true[0]
            dict_all[key1] = list_simple_title_true
print(dict_all)


for num1, i in enumerate(col1.find({},{"html":0})):
    flag = 0
    print(str(num1+1))
    try:
        company_name_judge = i['tag']['organization']


        simple_name_list = dict_all[company_name_judge]
        for each in simple_name_list:

            if (each in i['title']) or (each in i['content']):

                myquery = {"title": i["title"], "publish_time":i["publish_time"]}
                # newvalues = {"$unset": {"organization": ""}}
                newvalues = {"$set": {"valid": 1}}
                col1.update_one(myquery, newvalues)
                flag = 1
                break
        if flag == 1:
            continue
        else:
            myquery = {"title": i["title"], "publish_time": i["publish_time"]}
            # newvalues = {"$unset": {"organization": ""}}
            newvalues = {"$set": {"valid": 0}}
            col1.update_one(myquery, newvalues)
    except:
        col1.delete_one(i)
        num_delete += 1
        print("num_delete:", num_delete)


