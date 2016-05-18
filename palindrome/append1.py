def f(s):
    for k in range(len(s)):
        j = 0
        prejump = True
        for c in s:
            if prejump and j >= k:
                j = len(s)-1
                prejump = False
            if c != s[j]:
                break
            j = j+1 if prejump else j-1
        else:
            return k

print(f('aaa'))
print(f('aba'))
print(f('abcba'))
print(f('abb'))
print(f('abbb'))
print(f('abcb'))
print(f('abcbc'))
print(f('abc'))
