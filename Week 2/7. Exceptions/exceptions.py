# read number of test cases
t = int(input())

for _ in range(t):
    try:
        # read two inputs and convert to int
        a, b = input().split()
        a = int(a)
        b = int(b)
        # do integer division and print result
        print(a // b)
    except (ZeroDivisionError, ValueError) as e:
        # if there is an error, print it like shown
        print("Error Code:", e)
