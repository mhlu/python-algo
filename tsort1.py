from collections import defaultdict

G = {
    'a': set(['b', 'f'])
    ,'b': set(['c', 'd', 'f'])
    ,'c': set(['d'])
    ,'d': set(['e'])
    ,'e': set(['f'])
    ,'f': set()
}

def tsort(G):
    # dep[v] is in-degree of v
    dep = defaultdict(int)
    candidates = set()
    for k in G:
        for v in G[k]:
            dep[v] += 1
    for k in G: 
        if not dep[k]:
            candidates.add(k)

    if not candidates:
        return None

    sortedList = []
    while candidates:
        c = candidates.pop()
        sortedList.append(c)
        for v in G[c]:
            dep[v] -= 1
            if dep[v] == 0:
                candidates.add(v)

    return sortedList

print(tsort(G))
