def test_string_upper():
    assert "qa".upper() == "QA"


def test_string_strip():
    assert "    test    ".strip() == "test"


def test_replace_text():
    assert "monkey automation".replace("monkey", "QA") == "QA automation"


def test_replace_text():
    assert "monkey automation".replace("monkey", "QA") == "QA automation"
