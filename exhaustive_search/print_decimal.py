def print_decimal(digits):
    print_decimal_helper(digits, "")


def print_decimal_helper(digits, output):
    if digits == 0:
        print(output)
    else:
        for i in range(10):
            print_decimal_helper(digits - 1, output + str(i))


if __name__ == '__main__':
    print_decimal(10)
