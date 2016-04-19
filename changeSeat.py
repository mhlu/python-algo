# input is a directed graph ( with possible self arc )
# given the constraint that each node has an out-degree of exactly 1
# find a subgraph where each node has an indegree of exactly 1

from collections import defaultdict

test = {
    'a': 'c',
    'b': 'c',
    'c': 'a',
    'd': 'f',
    'e': 'd',
    'f': 'f',
    'g': 'h',
    'h': 'e'
}

def changeSeat(g):
    group = set(g.keys())
    kicked = set()
    indegree = defaultdict(int)

    for p in g:
        indegree[g[p]] += 1

    for p in g:
        if indegree[p] == 0:
            kicked.add(p)

    while kicked:
        p = kicked.pop()
        group.remove(p)
        indegree[g[p]] -= 1
        if indegree[g[p]] == 0:
            kicked.add(g[p])

    return group

print(changeSeat(test))





