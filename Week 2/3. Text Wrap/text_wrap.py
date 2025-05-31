import textwrap

def wrap(string, max_width):
    # I am Wrapping the string into lines of max_width using textwrap.fill
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)
