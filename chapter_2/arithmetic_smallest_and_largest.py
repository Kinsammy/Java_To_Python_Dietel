if __name__ == '__main__':

    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    third_number = int(input("Enter third number: "))

    total = first_number + second_number + third_number
    average = total // 3
    product = first_number * second_number * third_number

    smallest = first_number
    if second_number < smallest:
        smallest = second_number
    if third_number < smallest:
        smallest = third_number

    largest = first_number
    if second_number > largest:
        largest = second_number
    if third_number > largest:
        largest = third_number

    print("The sum is %d\n" % total)
    print("The average is %d\n" % average)
    print("The product is %d\n" % product)
    print("The Smallest is %d\nThe Largest is %d " % (smallest, largest))

