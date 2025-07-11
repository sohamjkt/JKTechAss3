import random
import importlib.util
import os
import inspect

PREPROCESS_FUNCS = {}
POSTPROCESS_FUNCS = []


functions_dir = os.path.join(os.path.dirname(__file__), "functions")
for filename in os.listdir(functions_dir):
    if filename.endswith(".py") and not filename.startswith("__"):
        module_name = filename[:-3]
        module_path = os.path.join(functions_dir, filename)
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        for name, obj in inspect.getmembers(mod):
            if inspect.isfunction(obj):
                if name.startswith("post_"):
                    POSTPROCESS_FUNCS.append(obj)
                else:
                    PREPROCESS_FUNCS[name] = obj


add = PREPROCESS_FUNCS.get("add")
multiply = PREPROCESS_FUNCS.get("multiply")
divide = PREPROCESS_FUNCS.get("divide")


def get_valid_input():
    while True:
        try:
            user_input = input("Enter at least two non-zero integers separated by spaces: ")
            numbers = list(map(int, user_input.strip().split()))
            non_zero_numbers = [num for num in numbers if num != 0]
            if len(non_zero_numbers) >= 2:
                return non_zero_numbers
            else:
                print("Please enter at least two non-zero integers.")
        except ValueError:
            print("Invalid input. Please enter integers only.")


def ensure_even_sum(numbers):
    attempts = 0
    while add and add(numbers) % 2 != 0 and attempts < 3:
        rand_num = random.choice([i for i in range(-10, 11) if i != 0])
        print(f"Sum is odd. Adding random number {rand_num} to the list.")
        numbers.append(rand_num)
        attempts += 1
    return numbers


def ensure_even_product(numbers):
    attempts = 0
    while multiply and multiply(numbers) % 2 != 0 and attempts < 3:
        rand_num = random.choice([i for i in range(-10, 11) if i != 0])
        print(f"Product is odd. Adding random number {rand_num} to the list.")
        numbers.append(rand_num)
        attempts += 1
    return numbers


def ensure_non_zero_last(numbers):
    if numbers[-1] == 0:
        rand_num = random.choice([i for i in range(-10, 11) if i != 0])
        print(f"Last number is zero. Replacing with random number {rand_num}.")
        numbers[-1] = rand_num
    return numbers


def main():
    numbers = get_valid_input()
    numbers = ensure_even_sum(numbers)
    numbers = ensure_even_product(numbers)
    numbers = ensure_non_zero_last(numbers)

    try:
        if divide is None:
            raise Exception("Divide function not loaded.")
        result = divide(numbers)
        print(f"Initial result (divide first/last): {result}")

        
        for func in POSTPROCESS_FUNCS:
            try:
                result = func(result)
                print(f"Result after {func.__name__}: {result}")
            except Exception as e:
                print(f"Error applying {func.__name__}: {e}")

    except ValueError as e:
        print(f"Error during division: {e}")


if __name__ == "__main__":
    main()
