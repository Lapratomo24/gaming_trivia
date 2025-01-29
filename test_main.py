import os
import pytest
from main import ensure_data_dir_exists, mode_validation, save_to_csv
from quiz import Quiz, DATA_DIR


# Test to ensure data directory exists
def test_ensure_data_dir_exists():
    if os.path.exists(DATA_DIR):
        os.rmdir(DATA_DIR)
    assert not os.path.exists(DATA_DIR)

    ensure_data_dir_exists()
    assert os.path.exists(DATA_DIR)

    os.rmdir(DATA_DIR)


# Test to validate user input for mode selection
def test_mode_validation():
    assert mode_validation("a") == True
    assert mode_validation("b") == True
    assert mode_validation("c") == True
    assert mode_validation("d") == False
    assert mode_validation("1") == False


SAMPLE_QUESTION = {
    "question": "What is the capital of France?",
    "options": ["Berlin", "Paris", "Madrid"],
    "answer": "Paris",
}

# Test to display question
def test_display_question(capsys):
    quiz = Quiz(SAMPLE_QUESTION)
    quiz.display_question(SAMPLE_QUESTION)
    captured = capsys.readouterr()
    assert "What is the capital of France?" in captured.out
    assert "1. Berlin" in captured.out
    assert "2. Paris" in captured.out
    assert "3. Madrid" in captured.out


if __name__ == "__main__":
    pytest.main()
