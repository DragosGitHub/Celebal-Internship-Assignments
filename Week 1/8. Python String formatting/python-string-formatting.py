def print_formatted(number):
    # Calculating the width of the binary representation of the max number
    width = len(bin(number)) - 2
    
    for i in range(1, number + 1):
        # It is Decimal representation, right aligned
        dec = str(i).rjust(width)
        # It is Octal representation, right aligned
        octal = oct(i)[2:].rjust(width)
        # It is Hexadecimal representation (uppercase), right aligned
        hexa = hex(i)[2:].upper().rjust(width)
        # Binary representation is here, right aligned
        binary = bin(i)[2:].rjust(width)
        
        # Printing all values in one line separated by a space
        print(dec, octal, hexa, binary)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)