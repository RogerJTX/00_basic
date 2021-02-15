import time
import pymongo
from tqdm import tqdm


client = pymongo.MongoClient('xxx', 1)
db1 = client.xxx
col1 = db1.xxx
count = col1.find().count()

import time
from tqdm import tqdm

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    # 设置描述
    pbar.set_description("Processing %s" % char)
    time.sleep(1)

import time
from tqdm import tqdm

# 一共200个，每次更新10，一共更新20次
with tqdm(total=200) as pbar:
  for i in range(20):
    pbar.update(10)
    time.sleep(0.1)

#方法2：
pbar = tqdm(total=200)
for i in range(20):
    pbar.update(10)
    time.sleep(0.1)
# close() 不要也没出问题？
pbar.close()