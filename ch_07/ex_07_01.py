# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case.

fname = input('Enter file name: ')
fhand = open(fname)
for lx in fhand :
    ly = lx.rstrip()
    print(ly.upper())
