# This module uses for main logic of the app
from logic.note_dataclass import Note

class NoteOperations:
    def __init__(self, list_of_notes):
        pass

    def show_topics(self):
        if list_of_notes:
            for note in list_of_notes:
                print(note.topic)
        else:
            print("There are'nt notes in note-app yet")

    def create_note(self):
        pass


    def edit_note(self):
        pass


    def delete_note(self):
        user_string: str = Validator.validate_str(
            input("What note do you want to delete. Enter your topic: "),
            "What note do you want to delete. Enter your topic: " )
        user_answer: bool = Validator.validate_y_or_n_str(input("Do you really"))
