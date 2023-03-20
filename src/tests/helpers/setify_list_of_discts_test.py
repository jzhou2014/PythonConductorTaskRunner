# tests the setify_list_of_dicts function
from helpers.setify_list_of_dicts import setify_list_of_dicts


def test_setify_list_of_dicts():
    assert setify_list_of_dicts(
        [
            {"a": 1, "b": 2},
            {"a": 1, "b": 2},
            {"a": 1, "b": 2},
            {"a": 1, "b": 2},
            {"a": 1, "b": 2},
        ]
    ) == [{"a": 1, "b": 2}]
