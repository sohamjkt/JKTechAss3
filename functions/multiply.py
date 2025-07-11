def multiply(numbers):
    """
    return the multiplication of all numbers in a list
    """
    result = 1
    for num in numbers:
        result *= num
    return result