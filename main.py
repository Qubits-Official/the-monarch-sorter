""" Program Flow
    1) Get the method of sorting (a or b).
    2) Get the number of monarchs to sort.
    3) Get the list of monarchs one line at a time.
    4) Sort the list according to the chosen method
    5) Print the results.
"""

from datetime import date


def main():
    # Get method type.
    method = input().lower()

    # Error handling for method type.
    if method not in ["a", "b"]:
        print("ERROR: Incorrect option")
        exit()

    # Get the number of monarchs.
    size = int(input())

    # Get the list of monarchs.
    monarchs = list()
    for _ in range(size):
        monarchs.append(input())

    # Test code.
    print(method, size, monarchs)

def roman_to_int(roman):
    """ Converts a roman numeral value into decimal. """

    roman = roman.upper()
    rom_dec_map = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    dec_sum = 0
    
    for index in range(len(roman)):
        try:
            value = rom_dec_map[roman[index]]

            # Perform subtration if the right adajacent value is bigger,
            # otherwise, perform addition.
            if (index + 1 < len(roman)) and (rom_dec_map[roman[index + 1]] > value):
                dec_sum -= value
            else:
                dec_sum += value
        except KeyError:    # Error if the roman numeral input does not exist.
            print("(1) input is not a valid Roman numeral")
            
    # Check if the parsed dec_sum is valid.
    # One way of doing this is converting the dec_sum
    # into roman numeral, then compare it to the original
    # roman numeral input.
    # This method works becuase decimal to roman numeral
    # is much easier to implement, and I am logically confident that
    # it gives the right answer.
    if roman_checker(dec_sum) == roman:
        return dec_sum
    else:
        print("(2) input is not a valid Roman numeral")

def sort_by_name(monarchs):
    pass

def sort_by_date(monarchs):
    pass

# Utility Function/s
def roman_checker(decimal):
    """ Converts a decimal value into a roman numeral. """

    # Roman numeral represented range: (1, 3999).
    if not 0 < decimal < 4000:
        print("Decimal value must be between 1 and 3999.")
    
    # Roman numeral constants and their decimal values.
    rom_const = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    dec_const = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    
    # Placeholder for the roman numeral build.
    rom_build = []
    
    for index in range(len(dec_const)):
        # Get how many roman constants per tier are there.
        # (starting from the biggest up to the lowest)
        multiplier = int(decimal / dec_const[index])
        
        # Build the roman numeral accordingly.
        # If a specific roman constant is not applicable,
        # the multiplier is equal to 0, thus not including
        # it in the build.
        rom_build.append(rom_const[index] * multiplier)
        
        # Update the decimal input.
        # Preparation for the next loop cycle.
        decimal -= dec_const[index] * multiplier
        
    return ''.join(rom_build)    # Transform the rom_build to string.

def parse_monarchs(monarchs):
    first_names = list()
    rom_num = list()
    dates = list()

    for monarch in monarchs:
        first_space = monarch.find(" ")
        second_space = monarch.find(" ", first_space+1)
        third_space = monarch.find(" ", second_space+1)
        comma_pos = monarch.find(",")

        first_names.append(monarch[:monarch.find(" ")])
        dates.append(monarch[comma_pos+1:])
     
    return dates

def to_dec_date(rom_dates):
    """ Convert the roman numerical date to decimal date. """

    dec_dates = list()
    for rom_date in rom_dates:
        first_dot = rom_date.find(".")
        second_dot = rom_date.find(".", first_dot+1)

        day = roman_to_int(rom_date[:first_dot])
        month = roman_to_int(rom_date[first_dot+1:second_dot])
        year = roman_to_int(rom_date[second_dot+1:])

        dec_dates.append()

    return dec_dates

def to_date_obj(dec_dates):
    """ Convert the decimal date into a date object. """

    date_objs = list()
    for date_obj in dec_dates:
        try:
            pass
        except:
            pass
        else:
            pass
    
    return date_objs


if __name__ == "__main__":
    main()
