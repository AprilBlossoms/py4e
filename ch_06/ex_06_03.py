# Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def count(str, ltr):
    num = 0
    for letter in str:
        if letter == ltr:
            num = num + 1
    return(num)

print(count('banana', 'a'))
