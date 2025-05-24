from itertools import combinations

# Reading number of letters in the list
N = int(input())

# Reading list of letters (space separated)
letters = input().split()

# Reading number of indices to be selected
K = int(input())

# Generating all possible combinations of size K from letters list
all_combinations = list(combinations(letters, K))

# Counting how many combinations contain at least one 'a'
count_with_a = sum(1 for combo in all_combinations if 'a' in combo)

# Calculating probability: combinations with 'a' divided by total combinations
probability = count_with_a / len(all_combinations)

# Printing probability rounded to 4 decimal places
print(f"{probability:.4f}")
