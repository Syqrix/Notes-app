# This module uses for main logic of the app
from logic.note_dataclass import Note
from utilities import Validator


class NoteOperations:
    def __init__(self, logic_check, notes_list):
        self.logic_check = logic_check
        self.notes_list = notes_list

    def show_topics(self) -> None:
        if self.notes_list.list_of_notes:
            for note in self.notes_list.list_of_notes:
                print(note.topic)
        else:
            print("There are'nt notes in note-app yet")

    def create_note(self) -> None:
        while True:
            user_topic: str = Validator.validate_str(
                input("Please enter your topic: "), "Please enter your topic: "
            )
            checker: bool = self.logic_check.check_for_note(user_topic.capitalize())
            if checker:
                print(
                    "Note-app already has this topic. You can have only one original topic. Try another one."
                )
                continue
            else:
                user_text: str = input("Please enter your text: ")
                new_object: object = Note(
                    user_topic.capitalize(), user_text.capitalize()
                )
                self.notes_list.list_of_notes.append(new_object)
                print("Note has been created!")
                break

    def open_note(self) -> None:
        user_input_topic: str = Validator.validate_str(
            input("What topic do you want to open? "),
            "What topic do you want to open? ",
        )
        note_check: bool = self.logic_check.check_for_note(
            user_input_topic.capitalize()
        )
        if note_check:
            data: Note = self.logic_check.return_note(user_input_topic.capitalize())
            print(data.text)
        else:
            print("There is no such topic in note-app")

    def edit_note(self) -> None:
        operations: dict = {1: "Topic", 2: "Text"}
        user_input_topic: str = Validator.validate_str(
            input("What note do you want to change? "),
            "What note do you want to change? ",
        )
        note_check: bool = self.logic_check.check_for_note(
            user_input_topic.capitalize()
        )
        if note_check:
            data: Note = self.logic_check.return_note(user_input_topic.capitalize())
            print("\n Available_operations: ")
            for key, text in operations.items():
                print(f"{key}: {text}")
        else:
            print("There is no such note in note-app")

        while True:
            user_answer: int = Validator.validate_int_number(
                input("\nWhat do you want to change? "), "\nWhat do you want to change?"
            )

            if user_answer not in operations:
                print(f"Only in this range: 0-{str(len(operations))}")
                continue
            else:
                break

        if user_answer == 1:
            new_topic: str = Validator.validate_str(input("New topic: "), "New topic: ")
            check: bool = self.logic_check.check_for_note(new_topic.capitalize())
            if check:
                user_check: bool = Validator.validate_y_or_n_str(
                    input(
                        "You already have this original topic. Do you want to add sufix (1,2 and etc) ? "
                    ),
                    "You already have this original topic. Do you want to add sufix (1,2 and etc) ? ",
                )
                if user_check:
                    last_character: str = data.topic[-1]
                    if last_character.isdigit():
                        last_character = str(int(last_character) + 1)
                        data.topic = new_topic.capitalize().replace(
                            new_topic[-1], last_character
                        )
                    else:
                        data.topic = (new_topic + "1").capitalize()
                else:
                    return
            else:
                data.topic = new_topic.capitalize()
        else:
            new_text: str = input("New text: ")
            data.text = new_text.capitalize()

    def delete_note(self) -> None:
        while True:
            user_input_topic: str = Validator.validate_str(
                input("What note do you want to delete. Enter your topic: "),
                "What note do you want to delete. Enter your topic: ",
            )
            answer_of_func: bool = self.logic_check.check_for_note(
                user_input_topic.capitalize()
            )
            if answer_of_func is False:
                continue
            else:
                break
        user_answer: bool = Validator.validate_y_or_n_str(
            input("Do you really want to delete this note? "),
            "Do you really want to delete this note? ",
        )
        if user_answer:
            data: Note = self.logic_check.return_note(user_input_topic.capitalize())
            self.notes_list.list_of_notes.remove(data)
            print("Note has been deleted!")
        else:
            return
