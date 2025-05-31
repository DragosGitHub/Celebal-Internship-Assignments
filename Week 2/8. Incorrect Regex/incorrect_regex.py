import re

# reading how many strings to check
t = int(input())

for _ in range(t):
    pattern = input()
    try:
        # trying to compile regex, if error means invalid regex
        re.compile(pattern)
        print("True")
    except re.error:
        # if exception comes, regex is invalid
        print("False")
