def function_with_flake_errors(number: int, second_number: int) -> None:
    try:
        number / second_number
    except ZeroDivisionError:
        print("You had an exception!")

