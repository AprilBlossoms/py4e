# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully
# by printing a message and exiting the program.

xh = input('Enter Hours: ')
xr = input('Enter Rate: ')
try:
    xp = float(xh) * float(xr)
    print('Pay:',xp)
except:
    print('Please enter a number')
