""" Program Flow
    1) Get the method of sorting (a or b).
    2) Get the number of monarchs to sort.
    3) Get the list of monarchs one line at a time.
    4) Sort the list according to the chosen method
    5) Print the results.
"""

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

def roman_to_decimal():
    pass



if __name__ == "__main__":
    main()
