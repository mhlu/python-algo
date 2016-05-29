def matrix_sum(matrix):
    if len(matrix) <= 0:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    return sum_helper(matrix, 0, 0, m, n)

def naive_sum(matrix):
    return sum(map(sum, matrix))

def sum_helper(matrix, si, sj, m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return matrix[si][sj]

    return sum_helper(matrix, si, sj, m//2, n//2) +\
            sum_helper(matrix, si+m//2, sj, m-m//2, n//2) +\
            sum_helper(matrix, si, sj+n//2, m//2, n-n//2) +\
            sum_helper(matrix, si+m//2, sj+n//2, m-m//2, n-n//2)

a = [
    [1,2,4,9],
    [1,3,4,9],
    [1,1,4,9],
    [1,2,4,9],
]
b = [
 [1,8,3,4,5,6,7],
 [1,8,3,3,5,6,7],
 [9,2,3,2,1,6,7],
 [1,2,9,4,5,1,7]
 ]
c = [[]]
d = [[], [], []]
print(matrix_sum(a) == naive_sum(a))
print(matrix_sum(b) == naive_sum(b))
print(matrix_sum(c) == naive_sum(c))
print(matrix_sum(d) == naive_sum(d))
