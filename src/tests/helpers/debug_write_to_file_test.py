# tests the debug_write_to_file function
import os
from helpers.debug_write_to_file import debug_write_to_file


def test_debug_write_to_file():
    os.environ["DEBUG"] = "true"
    debug_write_to_file("test", "test.txt", "w")
    assert os.path.exists("test.txt") is True
    os.environ["DEBUG"] = "false"
    os.remove("test.txt")
    assert os.path.exists("test.txt") is False
