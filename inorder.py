class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

def inorder(t):
    stack = [(t,1)]
    while stack:
        curr, status = stack.pop()
        if curr == None:
            continue
        if status == 1:
            stack.append((curr.r, 1))
            stack.append((curr, 0))
            stack.append((curr.l, 1))
        else:
            print(curr.v)

a = Node(3, Node(2), Node(4))
b = Node(8, Node(7))
c = Node(5, a, b)
print(c.r, c.l, a, b)
inorder(c)
