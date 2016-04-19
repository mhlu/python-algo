# a celebrity is a person who everyone follows but follows no-one

test_with_celebrity = {
    'a': set(),
    'b': {'c', 'a'},
    'c': {'b', 'a'},
    'd': {'a'},
    'e': {'b', 'a'}
}

test_without_celebrity = {
    'a': set(),
    'b': {'c', 'a'},
    'c': {'b', 'a'},
    'd': {'a'},
    'e': {'b'}
}


def celebrity(g):
    candidates = set(g.keys())
    while len(candidates) > 1:
        p1 = candidates.pop()
        p2 = candidates.pop()

        if p1 in g[p2]:
            candidates.add(p1)
        else:
            candidates.add(p2)

    if not candidates:
        return None, 't1'

    finalist = candidates.pop()
    if g[finalist]:
        return None, 't2'

    for p in g:
        if p != finalist and finalist not in g[p]:
            return None, 't3'

    return finalist

print(celebrity(test_with_celebrity))
print(celebrity(test_without_celebrity))
