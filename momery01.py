import psutil
import os
def memory_usage():
    mem_available = psutil.virtual_memory().available
    mem_process = psutil.Process(os.getpid()).memory_info().rss
    return round(mem_process / 1024 / 1024, 2), round(mem_available / 1024 / 1024, 2)

print(memory_usage())




