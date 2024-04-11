import pytest

from key_val_swap_solution import swap_dict_keys_and_value_lists

def test_empty_input():
    assert swap_dict_keys_and_value_lists({}) == {}

def test_single_key_single_value():
    assert swap_dict_keys_and_value_lists({"a": ["b"]}) == {"b": ["a"]}

def test_single_key_multiple_values():
    assert swap_dict_keys_and_value_lists({"a": ["b", "c"]}) == {"b": ["a"], "c": ["a"]}

def test_multiple_keys_multiple_values():
    assert swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) == {2: [1, 4], 3: [1], 5: [4]}
    
if __name__ == "__main__":
    pytest.main()