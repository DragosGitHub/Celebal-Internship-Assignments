n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    cmd = input().split()
    action = cmd[0]

    if action == 'pop':
        # I am removing an arbitrary element from the set
        s.pop()
    elif action == 'remove':
        val = int(cmd[1])
        # I am removing the value from the set; if it's not there, this will cause an error
        s.remove(val)
    elif action == 'discard':
        val = int(cmd[1])
        # I am removing the value from the set if it exists; no error if it does not
        s.discard(val)

# I am printing the sum of all remaining elements in the set
print(sum(s))
