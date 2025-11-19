# This module uses for logic check
from typing import Union


class LogicChecker:
    def __init__(self, notes_list):
        self.notes_list = notes_list


    def check_for_note(self, user_input: str) -> bool:
        self.notes_list.list_of_notes.sort(key=lambda note: note.topic)
        min: int = 0
        max: int = len(self.notes_list.list_of_notes) - 1

        while min <= max:
            avg: int = (max + min) // 2
            if self.notes_list.list_of_notes[avg].topic > user_input:
                max = avg - 1
                continue
            elif self.notes_list.list_of_notes[avg].topic < user_input:
                min = avg + 1
                continue
            else:
                return True

        return False

    def return_note(self, user_input: str) -> Union[object, None]:
        self.notes_list.list_of_notes.sort(key=lambda note: note.topic)
        min: int = 0
        max: int = len(self.notes_list.list_of_notes) - 1
        
        while min <= max:
            avg: int = (max + min) // 2
            if self.notes_list.list_of_notes[avg].topic > user_input:
                max = avg - 1
                continue
            elif self.notes_list.list_of_notes[avg].topic < user_input:
                min = avg + 1
                continue
            else:
                return self.notes_list.list_of_notes[avg]
        return None
