def notation(n):
    y = n**2 + 3*n + 1
    return y
"""
print(notation(2))
print(notation(3))
print(notation(4))
print(notation(5))

"""
anything = 0
for i in range (2,6):
    if i == 2: 
        print ('sum of the series: ')
    else:
        print('+')
    print (notation(i))

    anything = anything + notation(i)
print('=')
print (anything)
