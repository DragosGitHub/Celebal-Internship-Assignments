# This is the Function to calculate average of distinct heights
def average(array):
    # Converting list to set to remove duplicates
    distinct_heights = set(array)
    # Calculating the average of distinct heights
    return sum(distinct_heights) / len(distinct_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
