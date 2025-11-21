from logic import JsonDataManager, NoteOperations, Menu, NotesList
from logic.note_dataclass import Note
from utilities import LogicChecker
import pytest


@pytest.fixture
def fake_notes_list():
    return NotesList()


@pytest.fixture
def fake_json_manager(fake_notes_list):
    return JsonDataManager(fake_notes_list)


@pytest.fixture
def fake_menu(fake_note_operation, fake_json_manager):
    return Menu(fake_note_operation, fake_json_manager)


@pytest.fixture
def fake_logic_check(fake_notes_list):
    return LogicChecker(fake_notes_list)


@pytest.fixture
def fake_note_operation(fake_logic_check, fake_notes_list):
    fake_notes_list.list_of_notes.append(Note("True", "true"))
    return NoteOperations(fake_logic_check, fake_notes_list)


@pytest.fixture
def fake_note_operation_empty(fake_logic_check, fake_notes_list):
    return NoteOperations(fake_logic_check, fake_notes_list)
