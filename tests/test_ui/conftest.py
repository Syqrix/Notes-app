import pytest
from ui import Ui
from logic import JsonDataManager, NotesList


@pytest.fixture
def fake_notes_list():
    return NotesList()


@pytest.fixture
def fake_data_manager(fake_notes_list):
    return JsonDataManager(fake_notes_list)


@pytest.fixture
def fake_ui(fake_data_manager):
    return Ui(fake_data_manager)
