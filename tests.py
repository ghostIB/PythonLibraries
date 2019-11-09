import sys
import time
def TimeIt(func,*args):
    start=time.process_time()
    func(*args)
    return time.process_time()-start
def getSizeOfVariables(func,*args):
    sum=0
    for i in tuple(func(*args).values())[1:]:
        sum+=sys.getsizeof(i)
    return sum
def ComplexTest(func,*args):
    tic=time.process_time()
    variables=func(*args)
    tac=time.process_time()-tic
    sum=0
    for i in tuple(variables)[1:]:
        sum+=sys.getsizeof(i)
    return (tac,len(tuple(variables))-1,sum)