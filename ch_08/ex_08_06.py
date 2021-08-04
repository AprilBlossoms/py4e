# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers
# at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min()
# functions to compute the maximum and minimum numbers after the loop completes.

vals = []
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        print('Maximum is', max(vals))
        print('Minimum is', min(vals))
        break
    try :
        ival = int(sval)
        vals.append(ival)
    except :
        print('Invalid input')
