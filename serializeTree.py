from collections import deque
class Node:
    def __init__(self, v, children=None):
        if children is None:
            children = []
        self.children = children
        self.v = v
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

def serialize(t):
    s = str(t.v)
    for c in t.children:
        s += ' ' + serialize(c)
    s += ' |'
    return s

def deserialize(s):
    a = deque(s.split(' '))
    return dehelper(a)

def dehelper(a):
    n = Node(int(a[0]))
    a.popleft()
    while a[0] != '|':
        n.children.append(dehelper(a))
    a.popleft()
    return n

def dfs(t, l):
    print(t.v, l)
    for c in t.children:
        dfs(c, l+1)

a = Node(3, [Node(4), Node(5, [Node(7), Node(8)]), Node(6)])
b = serialize(a)
c = deserialize(b)
print(b)
print(a == c)
