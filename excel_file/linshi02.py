import pymongo
import copy
client = pymongo.MongoClient('xxx', 1)
db = client.xxx
col1 = db.xxx
col2 = db.xxx

list_a = []
# with open('manager.txt', 'r', encoding='utf-8') as f:
#     for i in f.readlines():
#         if '\t' in i:
#             name = i.split('\t')[0]
#         else:
#             name = i.strip()
#         list_a.append(name)
#         # print(name)
#
# list_b = set(list_a)
# for i_b in list_b:
#     count = 0
#     for i_a in list_a:
#         if i_b == i_a:
#             count += 1
#     print(i_b, ":", count)


list_company = []
with open('manager.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        if '\t' in i:
            name = i.split('\t')[1].replace('\n', '')
            list_company.append(name)

print(list_company)
flag = 0
for i_company in list_company:
    if i_company == '西北橡胶塑料研究设计院':
        flag = 1
    print(i_company)
    if flag == 1:
        for i in col1.find({'search_key':i_company}):
            search_key = i['search_key']
            publish_time = i['publish_time']
            title = i['title']
            pk = col2.find_one({'publish_time':publish_time, 'title':title})
            if not pk:
                col2.insert_one(i)
                print(search_key)


