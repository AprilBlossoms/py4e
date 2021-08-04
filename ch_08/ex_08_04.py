# Exercise 4: Find all unique words in a file
# Shakespeare used over 20,000 words in his works. But how would you determine that?
# How would you produce the list of all the words that Shakespeare used?
# Would you download all his work, read it and track all unique words by hand? Let’s use Python to achieve that instead.
# List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
# To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result.
# Write a program to open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words in alphabetical order.

fhand = open('romeo.txt')
unique_list = []

for line in fhand :
    line = line.split()
    for word in line :
        if word in unique_list:
            continue
        else:
            unique_list.append(word)
unique_list.sort()
print(unique_list)