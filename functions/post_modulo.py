def post_modulo(result):
    n = int(input("Enter a non-zero integer for modulo: "))
    if n == 0:
        raise ValueError("Cannot modulo by zero.")
    return result % n
