from collections import Counter

# read number of shoes in shop
n = int(input())
# read the sizes of the shoes and count how many we have of each size
shoe_sizes = Counter(map(int, input().split()))

# read number of customers coming
customers = int(input())

total_money = 0

# for each customer, check if shoe size is available
for _ in range(customers):
    size, price = map(int, input().split())
    # if shoe is available (count > 0)
    if shoe_sizes[size] > 0:
        total_money += price    # add the price to total money earned
        shoe_sizes[size] -= 1   # reduce count of that shoe size by 1

# print the total money earned after all customers
print(total_money)
