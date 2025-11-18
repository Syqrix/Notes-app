# This main module of the app
from ui.comunication import Ui
from logic import Menu, NotesList, NoteOperations
from utilities import Validator, LogicChecker



class App:
    def __init__(self, ui: Ui, menu: Menu):
        self.ui = ui
        self.menu = menu 


    def run(self) -> None:
        self.ui.say_hi()
        self.menu.choose_the_operation()
        self.ui.say_bye()


def main():
    # --- Data ---
    notes_list = NotesList()

    # ---Validators  and utilities---
    logic_checker = LogicChecker(notes_list)

    # --- Comunication ---
    ui = Ui()

    # --- Logic of app ---
    note_operations = NoteOperations(logic_checker, notes_list)

    menu = Menu(note_operations)
    app = App(ui, menu)
    app.run()


if __name__ == "__main__":
    main()
