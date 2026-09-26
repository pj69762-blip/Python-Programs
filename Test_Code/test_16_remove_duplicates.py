import importlib.util
from pathlib import Path

program_path = Path(__file__).resolve().parents[1] / "Code" / "16_remove_duplicates.py"

spec = importlib.util.spec_from_file_location("remove_duplicates", program_path)
program = importlib.util.module_from_spec(spec)
spec.loader.exec_module(program)


def test_remove_duplicates():
    assert program.remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert program.remove_duplicates([1, 1, 1, 2, 2]) == [1, 2]
    assert program.remove_duplicates([]) == []
    assert program.remove_duplicates([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]


if __name__ == "__main__":
    test_remove_duplicates()
    print("All test cases passed.")