# This module uses for comunication with uses
import sys


class Ui:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    @staticmethod
    def say_hi() -> None:
        print("Hi this is the Notes-app. Enjoy!")

    def say_bye(self) -> SystemExit:
        self.data_manager.save_data()
        print("Bye!")
        print("Exiting...")
        sys.exit()
