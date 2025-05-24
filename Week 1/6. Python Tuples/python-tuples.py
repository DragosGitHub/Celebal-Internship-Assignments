if __name__ == '__main__':
    n = int(input())  # Reading the number of elements
    integer_list = map(int, input().split())  # Reading the integers and convert to map object
    
    # Creating a tuple from the integer list
    t = tuple(integer_list)
    
    # Printing the hash of the tuple
    print(hash(t))
