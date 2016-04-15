def ssort(array):
    arr = array[:]

    for i in range(len(arr)-1, 0, -1):
        m = i
        for j in range(i+1):
            if arr[j] > arr[m]:
                m = j
        arr[m], arr[i] = arr[i], arr[m]

    return arr

