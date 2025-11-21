import pytest


class TestUi:
    @staticmethod
    def test_hi(fake_ui, capsys):
        fake_ui.say_hi()
        captured = capsys.readouterr()
        assert "Hi this is the Notes-app. Enjoy!" in captured.out

    @staticmethod
    def test_bye(fake_ui):
        try:
            with pytest.raises(SystemExit):
                fake_ui.say_bye()
        except FileNotFoundError:
            pass
