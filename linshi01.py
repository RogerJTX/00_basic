import pymongo
from bs4 import BeautifulSoup
client = pymongo.MongoClient('xxx', 0)
db1 = client.xxx
col1 = db1.xxx


for num, i in enumerate(col1.find()):
    print(num)
    _id = i['_id']
    html = i['html']
    soup = BeautifulSoup(html, 'lxml')
    tag1 = soup.find('div', {'class':'res_width institution_con'})
    if tag1:
        tag2 = tag1.find('img')['src']
        print(tag2)
        if tag2 == 'https://www.pedata.cn/images/logo_img.jpg':
            tag2 = ''

        myquery = {"_id": _id}
        newvalues = {"$set": {"logo_img_url": tag2}}

        col1.update_one(myquery, newvalues)
    else:
        print('没有找到src')
        break



