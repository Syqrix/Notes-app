# This module uses for menu logic
from utilities import Validator
import sys
import time

class Menu:
    def __init__(self, note_operation): 
        self.note_operation = note_operation

    
    def choose_the_operation(self) -> None:
        while True:
            operations: dict = {
                1: ("Show all topics and directories of notes in note-app",
                    self.note_operation.show_topics),
                2: ("Create note", self.note_operation.create_note),
                3: ("Open the note", self.note_operation.open_note), 
                4: ("Edit note", self.note_operation.edit_note),
                5: ("Delete note", self.note_operation.delete_note),
                6: ("Exit", self.exit_app)
            }

            print("\nAvailable_operations: ")
            for key, (text, _) in operations.items():
                print(f"{key}: {text}")

            while True:
                user_answer: int = Validator.validate_int_number(
                    input("\nWhat operation do you want to get? "),
                    "\nWhat operation do you want to get? ")

                if user_answer not in operations:
                    print(f"Only in this range: 0-{str(len(operations))}")
                    continue
                else:
                    _, func = operations[user_answer]
                    func()
                    break


    def exit_app(self) -> SystemExit:
        print("Exiting...")
        time.sleep(1)
        sys.exit()
