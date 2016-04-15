from math import ceil
def bisect(X, x):
    left = 0
    right = len(X)-1
    mid = (right+left)//2

    while left != right:
        if x < X[mid]:
            right = mid-1
        else:
            left = mid
        mid = ceil((right+left)/2)

    return mid
