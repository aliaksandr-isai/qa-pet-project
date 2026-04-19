import pytest


def multiply(a, b):
    return a * b


def test_sum():
    assert 1 + 1 == 2


def test_string_upper():
    assert "qa".upper() == "QA"


def test_string_strip():
    assert "    test    ".strip() == "test"


def test_replace_text():
    assert "monkey automation".replace("monkey", "QA") == "QA automation"


def test_multiply():
    assert multiply(2, 3) == 6


def test_list_contains():
    data = [1, 2, 3]
    assert 2 in data


def test_list_append():
    data = [1, 2, 3]
    data.append(4)
    assert data == [1, 2, 3, 4]


def test_list_length():
    data = [1, 2, 3]
    assert len(data) == 3


def test_list_remove():
    data = [1, 2, 3]
    data.remove(1)
    assert data == [2, 3]


def test_list_pop_last():
    data = [1, 2, 3]
    value = data.pop()
    assert value == 3
    assert data == [1, 2]


def test_list_pop_first():
    data = [1, 2, 3]
    value = data.pop(0)
    assert value == 1
    assert data == [2, 3]


def test_sort_list():
    data = [3, 2, 1]
    data.sort()
    assert data == [1, 2, 3]


def test_dict_value():
    user = {"name": "Alex", "age": 30}
    assert user["name"] == "Alex"
    assert user["age"] == 30


def test_dict_add_key():
    user = {}
    user["role"] = "QA"
    user["age"] = 30
    assert user == {"role": "QA", "age": 30}


def test_dict_missing_key():
    user = {}
    with pytest.raises(KeyError):
        user["role"]


def test_dict_get_method():
    user = {}
    assert user.get("role") is None