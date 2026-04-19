import pytest
from game.logic import VALID_ITEM_TYPES


@pytest.fixture
def sample_player():
    return {
        "name": "hero",
        "level": 3,
        "balance": 100,
        "inventory": []
    }


@pytest.fixture
def shop_item():
    return {
        "name": "Lightbringer",
        "type": "weapon",
        "price": 50
    }


def can_start_quest(player_level: int, required_level: int) -> bool:
    return player_level >= required_level


def can_purchase_item(balance: int, price: int) -> bool:
    return balance >= price


def is_valid_item_type(item_type: str) -> bool:
    return item_type in VALID_ITEM_TYPES


def test_player_start_with_empty_inventory(sample_player):
    assert sample_player["inventory"] == []


def test_player_has_not_empty_name(sample_player):
    assert sample_player["name"] != ""


def test_new_item_has_price(shop_item):
    assert shop_item["price"] > 0


def test_new_item_has_structure(shop_item):
    assert isinstance(shop_item["name"], str)
    assert isinstance(shop_item["type"], str)
    assert isinstance(shop_item["price"], int)



@pytest.mark.parametrize(
    "player_level, required_level, expected",
    [
        (2, 1, True),
        (1, 2, False),
        (3, 3, True),
    ],
)
def test_can_start_quest(player_level, required_level, expected):
    assert can_start_quest(player_level, required_level) is expected


@pytest.mark.parametrize(
    "balance, price, expected",
    [
        (100, 50, True),
        (50, 50, True),
        (50, 100, False),
        (0, 50, False),
    ],
)
def test_can_purchase_item(balance, price, expected):
    assert can_purchase_item(balance, price) is expected


@pytest.mark.parametrize(
    "item_type, expected",
    [
        ("weapon", True),
        ("armor", True),
        ("consumable", True),
        ("skin", True),
        ("pet", False),
        ("", False),
    ],
)
def test_is_valid_item_type(item_type, expected):
    assert is_valid_item_type(item_type) is expected

