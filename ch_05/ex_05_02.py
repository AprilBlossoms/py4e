# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead of the average.

min = 'none'
max = 'none'
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        print('Maximum is', max)
        print('Minimum is', min)
        break
    try :
        ival = int(sval)
        if min == 'none' or min > ival :
            min = ival
        if max == 'none' or max < ival :
            max = ival
    except :
        print('Invalid input')
