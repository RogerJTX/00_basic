import pymongo

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
with open('expert_2020_07_24.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        if '\t' in i:
            name = i.split('\t')[0]
            list_company.append(name)

print(list_company)
for i_company in list_company:
    for i in col1.find({'search_key':i_company}):
        search_key = i['search_key']
        col2.insert_one(i)
        print(search_key)
