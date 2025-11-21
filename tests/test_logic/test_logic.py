class TestNoteOperations:
    class TestShowNotes:
        @staticmethod
        def test_show_notes_empty(fake_note_operation_empty, capsys):
            fake_note_operation_empty.show_topics()
            captured = capsys.readouterr()
            assert "There aren't notes in note-app yet" in captured.out

        @staticmethod
        def test_show_notes(fake_note_operation, capsys):
            fake_note_operation.show_topics()
            captured = capsys.readouterr()
            assert "True" in captured.out

    class TestCreateNote:
        @staticmethod
        def test_create_notes(fake_note_operation, capsys, monkeypatch):
            inputs = iter(["true", "New", "text"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_note_operation.create_note()
            captured = capsys.readouterr()
            assert "You have this topic, it's original. Try another one." in captured.out
            assert "Note has been created!" in captured.out

    class TestOpenNote:
        @staticmethod
        def test_open_notes_wrong_data(
                fake_note_operation, capsys, monkeypatch):
            input = "another"
            monkeypatch.setattr("builtins.input", lambda _: input)
            fake_note_operation.open_note()
            captured = capsys.readouterr()
            assert "There is no such topic in note-app" in captured.out

        @staticmethod
        def test_open_notes(fake_note_operation, capsys, monkeypatch):
            input = "true"
            monkeypatch.setattr("builtins.input", lambda _: input)
            fake_note_operation.open_note()
            captured = capsys.readouterr()
            assert "true" in captured.out

    class TestEditNote:
        @staticmethod
        def test_edit_topic_notes(fake_note_operation, capsys, monkeypatch):
            inputs = iter(["true", "3", "1", "true", "y"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_note_operation.show_topics()
            fake_note_operation.edit_note()
            fake_note_operation.show_topics()
            captured = capsys.readouterr()
            assert "Only in this range: 1-2" in captured.out
            assert "True" and "True1" in captured.out

    class TestDeleteNote:
        @staticmethod
        def test_delete_topic_notes(fake_note_operation, capsys, monkeypatch):
            inputs = iter(["true", "y"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_note_operation.show_topics()
            fake_note_operation.delete_note()
            fake_note_operation.show_topics()
            captured = capsys.readouterr()
            assert "True" in captured.out
            assert "Note has been deleted!" in captured.out
            assert "There aren't notes in note-app yet" in captured.out


class TestMenu:
    @staticmethod
    def test_menu(fake_menu, capsys, monkeypatch):
        try:
            inputs = iter(["7", "3", "true"])
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            fake_menu.choose_the_operation()
            captured = capsys.readouterr()
            assert "Only in this range: 1-6" in captured.out
            assert "True" in captured.out
        except StopIteration:
            pass
