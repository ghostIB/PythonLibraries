import numpy as np
def levenshtain(s,t):
    column=len(t)+1
    rows=len(s)+1
    distance=np.zeros((rows,column),dtype=int)
    distance[:,0]=np.arange(rows)
    distance[0,:]=np.arange(column)
    for col in range(1, column):
        for row in range(1, rows):
            cost= 0 if s[row-1]==t[col-1] else 2
            distance[row][col] = min(distance[row-1][col] + 1,
                                 distance[row][col-1] + 1,
                                 distance[row-1][col-1] + cost)
    rate=((len(s)+len(t)) - distance[-1][-1]) / (len(s)+len(t))
    return rate
def countChanges(s,t):
    column=len(t)+1
    rows=len(s)+1
    distance=np.zeros((rows,column),dtype=int)
    distance[:,0]=np.arange(rows)
    distance[0,:]=np.arange(column)
    for col in range(1, column):
        for row in range(1, rows):
            cost= 0 if s[row-1]==t[col-1] else 2
            distance[row][col] = min(distance[row-1][col] + 1,
                                 distance[row][col-1] + 1,
                                 distance[row-1][col-1] + cost)
    return distance[-1][-1]