#进程cpu
from  test import *
import multiprocessing 
import time

jobs = []

t = time.time()
for i in range(10):
    p = multiprocessing.Process\
    (target = count,args = (1,1))
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print("process cpu:",time.time() - t)