def is_leap(year):
    leap = False
    
    # Check if year is divisible by 4
    if year % 4 == 0:
        # Check if year is divisible by 100
        if year % 100 == 0:
            # Check if year is divisible by 400
            if year % 400 == 0:
                leap = True  # divisible by 400 means leap year
            else:
                leap = False  # divisible by 100 but not by 400 means NOT leap
        else:
            leap = True  # divisible by 4 but not by 100 means leap year
    else:
        leap = False  # not divisible by 4 means NOT leap year

    return leap

year = int(input())
print(is_leap(year))
