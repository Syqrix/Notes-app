import pytest


class TestLogicChecker:
    class TestNoteBoolChecker:
        @staticmethod
        def test_checker_for_note_true(fake_logic_checker):
            result = fake_logic_checker.check_for_note("True")
            assert result

        @staticmethod
        def test_checker_for_note_false(fake_logic_checker):
            result = fake_logic_checker.check_for_note("False")
            assert not result

    class TestNoteObjChecker:
        @staticmethod
        def test_checker_for_return_note_true(fake_logic_checker):
            result = fake_logic_checker.return_note("True")
            assert result.topic == "True"

        @staticmethod
        def test_checker_for_return_note_none(fake_logic_checker):
            result = fake_logic_checker.return_note("False")
            assert result is None


class TestValidators:
    class TestStrValidator:
        @staticmethod
        def test_str_validator(fake_validator, capsys, monkeypatch):
            inputs = iter(["5", "True"])
            fake_string = "Fake"
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            result = fake_validator.validate_str("", fake_string)
            captured = capsys.readouterr()
            assert "It's empty. Please enter something." in captured.out
            assert "Olny letters. Try again." in captured.out
            assert result == "True"

        @staticmethod
        def test_str_validator_exit(fake_validator):
            fake_string = "Fake"
            with pytest.raises(SystemExit):
                fake_validator.validate_str("Q", fake_string)

    class TestYAndNValidator:
        @staticmethod
        def test_y_and_n_validator_validations(
                fake_validator, capsys, monkeypatch):
            inputs = iter(["5", "word", "Ye"])
            fake_string = "Fake"
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            result = fake_validator.validate_y_or_n_str("", fake_string)
            captured = capsys.readouterr()
            assert "It's empty. Please enter something." in captured.out
            assert "Olny letters. Try again." in captured.out
            assert "Wrong value. Try again." in captured.out
            assert result

        @staticmethod
        def test_y_and_n_validator_values_check(
                fake_validator, capsys, monkeypatch):
            true_values = ["Y", "Ye", "Yes"]
            false_values = ["N", "No"]
            fake_string = "Fake"
            for i in true_values:
                assert fake_validator.validate_y_or_n_str(i, fake_string)

            for i in false_values:
                assert not fake_validator.validate_y_or_n_str(i, fake_string)

        @staticmethod
        def test_str_validator_exit(fake_validator):
            fake_string = "Fake"
            with pytest.raises(SystemExit):
                fake_validator.validate_y_or_n_str("Q", fake_string)

    class TestIntValidator:
        @staticmethod
        def test_int_validator(fake_validator, capsys, monkeypatch):
            inputs = iter(["text", "5"])
            fake_string = "Fake"
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            result = fake_validator.validate_int_number("", fake_string)
            captured = capsys.readouterr()
            assert "It's empty. Please enter something" in captured.out
            assert "Only numbers. Please try again" in captured.out
            assert result == 5

        @staticmethod
        def test_int_validator_exit(fake_validator):
            fake_string = "Fake"
            with pytest.raises(SystemExit):
                fake_validator.validate_int_number("Q", fake_string)
