import heapq

TEST = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def blocked(arr, seen, i, j):
    if len(arr) <= 0:
        return True
    if 0 <= i and i < len(arr)\
            and 0 <= j and j < len(arr[0])\
            and (arr[i][j] == 0 or arr[i][j] == 3)\
            and seen[i][j] == 0:
        return False

    return True

# this is poorly written cus I expirimented with it too much
def findPath(arr):
    if len(arr) <= 0:
        return 0
    seen = [ [0]*len(arr[0]) for i in range(len(arr)) ]
    empty = [ [0]*len(arr[0]) for i in range(len(arr)) ]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 2:
                si, sj = i, j

    h = [(0, si, sj)]
    heapq.heapify(h)

    for r in arr:
        print r

    while h:
        d, i, j = heapq.heappop(h)

        if arr[i][j] == 3:
            print(d)
            ii, jj = i, j
            while True:
                empty[ii][jj] = 1
                if arr[ii][jj] == 2:
                    break
                ii, jj = seen[ii][jj]
            for r in empty:
                print r
            return

        for mi, mj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if not blocked(arr, seen, i+mi, j+mj):
                seen[i+mi][j+mj] = (i, j)
                heapq.heappush(h, (d+1, i+mi, j+mj))

    return -1

print(findPath(TEST))
