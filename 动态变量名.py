names = globals()
for i in range(10):
    names['haha{0}'.format(i)] = i

print(haha1)
