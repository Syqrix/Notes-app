# This module uses for validation numbers
import sys


class Validator:
    @staticmethod
    def validate_int_number(user_input: str, string: str) -> int:
        while True:
            if user_input.lower() == "q":
                sys.exit()
            elif not user_input:
                print("It's empty. Please enter something")
                user_input = input(string)
                continue
            elif not user_input.isdigit():
                print("Only numbers. Please try again")
                user_input = input(string)
                continue
            else:
                return int(user_input)

    @staticmethod
    def validate_y_or_n_str(user_input: str, string: str) -> bool:
        while True:
            if user_input.lower() == "q":
                sys.exit()
            elif not user_input:
                print("It's empty. Please enter something.")
                user_input = input(string)
                continue
            elif user_input.isdigit():
                print("Olny letters. Try again.")
                user_input = input(string)
                continue
            elif user_input.lower() in ["y", "ye", "yes"]:
                return True
            elif user_input.lower() in ["n", "no"]:
                return False
            else:
                print("Wrong value. Try again.")
                user_input = input(string)
                continue

    @staticmethod
    def validate_str(user_input: str, string: str) -> str:
        while True:
            if user_input.lower() == "q":
                sys.exit()
            elif not user_input:
                print("It's empty. Please enter something.")
                user_input = input(string)
                continue
            elif user_input.isdigit():
                print("Olny letters. Try again.")
                user_input = input(string)
                continue
            else:
                return user_input
