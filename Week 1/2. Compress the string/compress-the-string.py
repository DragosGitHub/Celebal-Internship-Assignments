from itertools import groupby

#I am taking input from user
s = input()

#I am using groupby to group consecutive characters
for key, group in groupby(s):
    count = len(list(group))  # counting how many times the character is repeated
    print((count, int(key)), end=' ')  # printing the tuple with space in the end
