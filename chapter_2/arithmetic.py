if __name__ == '__main__':
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    first_number_square = first_number * first_number
    second_number_square = second_number * second_number

    total = first_number + second_number
    difference = first_number - second_number

    print("The Square of the first number: %d\n" % first_number_square)
    print("The Square of the first number: %d\n" % second_number_square)
    print("The difference between the squares: %d\n" % total)
    print("The difference between the squares: %d" % difference)
