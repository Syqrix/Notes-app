# This module uses for logic check


class LogicChecker:
    def __init__(self):
        self.list_of_notes = list_of_notes


    def check_for_note(user_input: str) -> bool:
        sorted_list_of_notes = sort(self.list_of_notes)
        min = 0
        max = len(self.list_of_notes) - 1
        avg = (max + min) / 2
        
        while min <= max:
            if sorted_list_of_notes[avg].topic < user_input:
                max = avg - 1
                continue
            elif sorted_list_of_notes[avg].topic < user_input:
                min = avg + 1
                continue
            else:
                return True
        print("There is no such note in note-app")
        return False
