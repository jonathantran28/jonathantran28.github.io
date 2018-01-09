print ('Enter a number: ')
x = int(input())

def fib(n):
    first = 1
    second = 1
    sume = 2
    print (first)
    print (second)
    for i in range(n-2):
        third = first + second
        print (third)
        first = second
        second = third
        sume = sume + third
    print(' The sum of the number you choose is: '+ str(sume))

fib(x)
