# This main module of the app
from ui import Ui
from logic import Menu, NotesList, NoteOperations, JsonDataManager
from utilities import LogicChecker


class App:
    def __init__(self, ui: Ui, menu: Menu, data_manager: JsonDataManager):
        self.ui = ui
        self.menu = menu
        self.data_manager = data_manager

    def run(self) -> None:
        self.data_manager.check_folder()
        self.data_manager.load_data()
        self.ui.say_hi()
        self.menu.choose_the_operation()
        self.ui.say_bye()


def main():
    # --- Data ---
    notes_list = NotesList()
    data_manager = JsonDataManager(notes_list)

    # ---Validators  and utilities---
    logic_checker = LogicChecker(notes_list)

    # --- Comunication ---
    ui = Ui(data_manager)

    # --- Logic of app ---
    note_operations = NoteOperations(logic_checker, notes_list)

    menu = Menu(note_operations, data_manager)
    app = App(ui, menu, data_manager)
    app.run()


if __name__ == "__main__":
    main()
