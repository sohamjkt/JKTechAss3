def divide(numbers):
    """
    return the division of first/last numbers in a list
    """
    if numbers[-1] == 0:
        raise ValueError("Cannot divide by zero.")
    return round(numbers[0] / numbers[-1])
