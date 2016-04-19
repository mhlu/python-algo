from random import randrange
from collections import defaultdict
test = [randrange(16) for i in range(64)]

def countingSort(arr):
    cnt = defaultdict(int)
    for n in arr:
        cnt[n]+=1 
    minNum = min(arr)
    maxNum = max(arr)
    B = [0] * (maxNum-minNum+1)

    idx = 0
    for n in range(minNum, maxNum+1):
        i = n - minNum
        B[i] = idx
        idx += cnt[i]

    A = [0]*len(arr)
    for n in arr:
        i = n-minNum
        A[B[i]] = n
        B[i] += 1

    return A


res = countingSort(test)
print(res)
print( 'Correct' if res == sorted(test) else 'Incorrect' )


