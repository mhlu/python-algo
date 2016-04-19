# given a graph and an integer k<=n  find a subgraph search that every
# node in subgraph has at least k neighbours

test = {
    'a': {'b', 'c', 'd'},
    'b': {'a'},
    'c': {'a', 'd'},
    'd': {'a', 'c'}
}

def party(g, k):
    kicked = set()
    left = set(g.keys())
    num_friends = {}
    for p in g:
        num_friends[p] = len(g[p])


    for p in g:
        if num_friends[p] < k:
            kicked.add(p)

    while kicked:
        p = kicked.pop()
        left.remove(p)
        for f in g[p]:
            num_friends[f] -= 1
            if num_friends[f] < k:
                kicked.add(f)
    return left

print(party(test, 2))


