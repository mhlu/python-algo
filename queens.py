def nqueens(r,n,p):
    cols = range(len(p))
    if not(len(p) == len(set(p[i] + i for i in cols)) == len(set(p[i] - i for i in cols))):
        return 0

    if r == n:
      print(p)
      return 1

    count = 0
    for c in set(range(n)) - set(p):
        count += nqueens(r + 1, n, p + [c])

    return count


print(8, nqueens(0,8,[]))

