import json
from pathlib import Path
from logic.note_dataclass import Note


class JsonDataManager:
    def __init__(self, notes_list):
        self.path_to_data = Path("data")
        self.path_to_data_file = Path("data/json_data.json")
        self.notes_list = notes_list

    def check_folder(self) -> None:
        if not self.path_to_data.exists():
            self.path_to_data.mkdir()
        else:
            pass

    def save_data(self) -> None:
        with open(self.path_to_data_file, "w") as file:
            data: dict = {
                "notes": [
                    {"topic": note.topic, "text": note.text}
                    for note in self.notes_list.list_of_notes
                ]
            }
            json.dump(data, file, indent=4)

    def load_data(self) -> None:
        self.notes_list.list_of_notes.clear()
        if not self.path_to_data_file.exists():
            self.path_to_data_file.touch()
        if self.path_to_data_file.stat().st_size == 0:
            return

        with open(self.path_to_data_file, "r") as file:
            data: dict = json.load(file)
            data_of_notes: dict = data["notes"]
            for note in data_of_notes:
                new_note: object = Note(
                    topic=note.get("topic"), text=note.get("text"))
                self.notes_list.list_of_notes.append(new_note)
