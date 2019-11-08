import sys
import time
def getSpeed(func,*args):
    start=time.process_time()
    func(*args)
    return time.process_time()-start
def getSizeOfVariables(func,*args):
    sum=0
    for i in tuple(func(*args).values())[1:]:
        sum+=sys.getsizeof(i)
    return sum