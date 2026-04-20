import pytest
from game.logic import (
    VALID_ITEM_TYPES,
    is_valid_item_type,
    can_start_quest,
    can_purchase_item,
    can_afford,
    buy_item,
    calculate_purchase_reward,
)


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


def test_can_afford_return_true_when_balance_is_enough():
    assert can_afford(100, 50) is True


def test_can_afford_return_false_when_balance_is_not_enough():
    assert can_afford(50, 100) is False


def test_buy_item_return_update_balance():
    assert buy_item(100, 50) == 50


def test_calculate_reward_returns_total_reward():
    assert calculate_purchase_reward(100, 50) == 15


def test_can_afford_returns_false_when_balance_is_lower_than_price():
    assert can_afford(49, 50) is False


def test_can_afford_raises_error_for_negative_balance():
    with pytest.raises(ValueError):
        can_afford(-10,50)


def test_can_afford_raises_error_for_negative_price():
    with pytest.raises(ValueError):
        can_afford(50,-10)


def test_buy_item_raises_error_when_balance_is_not_enough():
    with pytest.raises(ValueError):
        buy_item(10, 50)


def test_buy_item_raises_error_with_clear_message_for_negative_price():
    with pytest.raises(ValueError, match="Price can't be negative"):
        buy_item(10, -50)
