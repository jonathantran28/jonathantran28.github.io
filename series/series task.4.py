from math import factorial, pi
import time

def taylor(x):
    series = 0
    for i in range (16):
        a = ((-1)**i)*(x**(2*i))/(factorial(2*i))
        series = series + a
    return series


def deg_to_rad(deg):
    radian = deg * math.pi / 180
    return radian

print ('Sup man. I can calculate the cosine of any value. ')
time.sleep(2)
print ('Pick either Radians or Degrees?')
time.sleep(2)
choice = input(('Type "radians" for Radians or type "degrees" for Degrees. '))
choice = choice.lower()

if choice == "radians":
    x = float(input('think of a number and enter the number for radians: '))

elif choice == "degrees":
    x = float(input('Think of a number and enter the number for degrees: '))
    x = deg_to_rad(x)

print ('Lets see. The cosine of your value is: ')
print(taylor(x))
