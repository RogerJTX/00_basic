import datetime
import time
starttime = datetime.datetime.now()

time.sleep(8)
endtime = datetime.datetime.now()

print((endtime - starttime).seconds)
print(type((endtime - starttime).seconds))
