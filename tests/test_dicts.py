import pytest

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
