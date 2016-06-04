def permHelper(a, s, e):
    if s == e-1:
        yield a
    for i in range(s, e):
        a[s], a[i] = a[i], a[s]
        for p in permHelper(a, s+1, e):
            yield p

def perm(a):
    return permHelper(a, 0, len(a))

for p in perm([1,2,3]):
    print(p)
