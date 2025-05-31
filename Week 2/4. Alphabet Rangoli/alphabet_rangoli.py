def print_rangoli(size):
    # this is the alphabet string i will use to pick letters
    alphabet_str = "abcdefghijklmnopqrstuvwxyz"
    
    pattern_lines = []
    
    # making each line of the rangoli pattern here
    for level in range(size):
        # getting the letters from current level till the end
        slice_letters = alphabet_str[level:size]
        
        # joining letters with dash and then making it symmetric
        left_side = "-".join(slice_letters)
        full_pattern = left_side[::-1] + left_side[1:]
        
        pattern_lines.append(full_pattern)
    
    # find the length of the biggest line for centering later
    max_width = len(pattern_lines[0])
    
    # printing top half of the rangoli (without the middle line)
    for idx in range(size - 1, 0, -1):
        print(pattern_lines[idx].center(max_width, '-'))
    
    # printing the middle line and the bottom half
    for idx in range(size):
        print(pattern_lines[idx].center(max_width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
