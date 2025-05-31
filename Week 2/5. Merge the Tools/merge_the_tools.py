def merge_the_tools(string, k):
    # how many chunks of size k we will have
    n = len(string) // k
    
    # go through each chunk
    for i in range(n):
        # get the current chunk from the string
        part = string[i*k : (i+1)*k]
        
        seen = set()  # keep track of letters we already took
        result = []   # store letters for this chunk without repeats
        
        # check every letter in the chunk
        for ch in part:
            # if this letter is not added before, add it
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        
        # print the final chunk with no repeats
        print("".join(result))

if __name__ == '__main__':
    s = input()
    k = int(input())
    merge_the_tools(s, k)
