# This module uses for menu logic
from utilities.validators import Validator
import sys

class Menu:
    def __init__(self):
        pass

    
    def choose_the_operation(self) -> None:
        operations: dict = {
            1: "Show all topics of notes in note-app",
            2: "Create note",
            3: "Edit note",
            4: "Delete note",
            5: "Exit",
        }

        print("Avaibales operations:\n")
        for key, value in operations.items():
            print(f"{key}: {value}")

        while True:
            user_answer: int = Validator.validate_int_number(
                input("What operation do you want to get? "),
                "What operation do you want to get? ")

            if user_answer not in operations:
                print(f"Only in this range: 0-{str(len(operations))}")
                continue
            else:
                #Here shold be logic for executing functions
                pass


    def exit_app(self) -> SystemExit:
        print("Exiting...")
        sys.exit()
