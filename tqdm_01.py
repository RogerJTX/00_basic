from tqdm import tqdm
import time
from tqdm._tqdm import trange


for i in tqdm(range(50)):
    time.sleep(0.1)
    pass

for j in trange(50):
    time.sleep(0.05)