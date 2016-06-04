def power(x,y):
    if y == 0:
        return 1
    if y == 1:
        return x
    tmp = power(x, y//2)
    print(tmp)
    if y%2 == 0:
        return tmp*tmp
    else:
        return tmp*tmp*x

print(power(2,3), 2**3)
print(power(3,5), 3**5)
