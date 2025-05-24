def minion_game(string):
    vowels = 'AEIOU'  #it is the vowels list
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    # Here it is Looping over each starting position in the string
    for i in range(length):
        # If the first letter is vowel, adding substrings count to Kevin
        if string[i] in vowels:
            kevin_score += (length - i)
        else:
            # Otherwise adding to Stuart's score
            stuart_score += (length - i)

    # Determining the winner and printing result
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input().strip().upper()  #It is the input string in uppercase (safe)
    minion_game(s)
