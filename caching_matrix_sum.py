def create_cache(matrix, si, sj, m, n, cache):
    if (si, sj, m, n) in cache:
        return

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            create_cache(matrix, si+i, sj+j, m-i, n-j, cache)

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                cache[(si,sj,i,j)] = 0
            elif i == 1 and j == 1:
                cache[(si,sj,i,j)] = matrix[si][sj]
            else:
                leftTop = cache[(si, sj, 1, 1)] 
                leftBot = cache[(si+1, sj, i-1, 1)] if i>1 else 0
                rightTop = cache[(si, sj+1, 1, j-1)] if j>1 else 0
                rightBot = cache[(si+1, sj+1, i-1, j-1)] if i>1 and j>1 else 0
                cache[(si, sj, i, j)] = leftTop+leftBot+rightTop+rightBot

def naiveSum(matrix):
    return sum(map(sum, matrix))

def test_cache_sum(matrix):
    cache = {}
    if len(matrix) <= 0:
        return 0
    create_cache(matrix, 0, 0, len(matrix), len(matrix[0]), cache)
    return cache[(0,0,len(matrix),len(matrix[0]))]



a = [ 
    [1,1,1],
    [1,2,2],
    [1,2,3]
]
b = [ 
[1,8,3,4,5,6,7],
[1,8,3,3,5,6,7],
[9,2,3,2,1,6,7],
[1,2,9,4,5,1,7] 
]
print(naiveSum(a) == test_cache_sum(a))
print(naiveSum(b) == test_cache_sum(b))
