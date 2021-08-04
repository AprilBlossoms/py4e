# Exercise 1: Write a while loop that starts at the last character in the string
# and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

def print_backwards(str):
    i = len(str)
    while i > 0:
        print(str[i-1])
        i = i - 1

print_backwards('cat')
