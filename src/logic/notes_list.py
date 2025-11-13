# This module uses for keeping objects(Notes)
from dataclasses import dataclass, field
from logic.note_dataclass import Note


@dataclass
class NotesList:
    list_of_notes: list[Note] = field(default_factory=list)
