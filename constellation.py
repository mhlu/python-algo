from collections import deque

TEST = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [ 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [ 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
] # 7

def blocked(arr, seen, i, j):
    if len(arr) <= 0:
        return True

    if 0 <= i and i < len(arr)\
        and 0 <= j and j < len(arr[0])\
        and arr[i][j] == 1\
        and seen[i][j] == False:
        return False
    return True

def count(arr):
    if len(arr) <= 0:
        return 0
    seen = [ [0]*len(arr[0]) for i in range(len(arr)) ]

    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if not blocked(arr, seen, i, j):
                cnt += 1
                q = deque([(i,j)])
                while q:
                    ei, ej = q.popleft()
                    seen[ei][ej] = True
                    for (mi, mj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if not blocked(arr, seen, ei+mi, ej+mj):
                            q.append((ei+mi, ej+mj))
    return cnt

print(count(TEST))
