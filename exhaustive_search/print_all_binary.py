def print_all_binary(digits):
    print_all_binary_helper(digits, "")


def print_all_binary_helper(digits, output):
    # To print 3-digit
    #   print 0
    #   print 2-digit binary number
    #   print 1
    #   print 2-digit binary number

    # Base case: 0-digit binary number
    #   print output
    if digits == 0:
        print(output)
    else:
        print_all_binary_helper(digits - 1, output + "0")
        print_all_binary_helper(digits - 1, output + "1")


if __name__ == '__main__':
    print_all_binary(3)
