from bisect import bisect
def isort(array):
    arr = array[:]

    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        value = arr[i]
        idx = bisect(arr, value, 0, i)
        arr[idx+1:i+1] = arr[idx:i]
        arr[idx] = value

    return arr
