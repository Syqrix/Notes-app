import pytest
from utilities import LogicChecker, Validator
from logic import NotesList
from logic.note_dataclass import Note


@pytest.fixture
def fake_list_of_notes():
    return NotesList()


@pytest.fixture
def fake_logic_checker(fake_list_of_notes):
    fake_list_of_notes.list_of_notes.append(Note("True", "true"))
    return LogicChecker(fake_list_of_notes)


@pytest.fixture
def fake_validator():
    return Validator()
