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


def can_afford(balance: int, price: int) -> bool:
    if balance < 0:
        raise ValueError("Balance can't be negative")
    if price < 0:
        raise ValueError("Price can't be negative")
    return balance >= price


def buy_item(balance: int, price: int) -> int:
    if balance < 0:
        raise ValueError("Balance can't be negative")
    if price < 0:
        raise ValueError("Price can't be negative")
    if balance < price:
        raise ValueError("Not enough money")
    return balance - price


def calculate_purchase_reward(price: int, bonus_percent: int) -> int:
    if price < 0:
        raise ValueError("Price can't be negative")
    if bonus_percent < 0:
        raise ValueError("Bonus_percent can't be negative")
    base_reward = price // 10
    bonus = base_reward * bonus_percent // 100
    total_reward = base_reward + bonus
    return total_reward

def test_can_afford_return_true_when_balance_is_enough():
    assert can_afford(100, 50) == True


def test_can_afford_return_false_when_balance_is_not_enough():
    assert can_afford(50, 100) == False


def test_buy_item_return_update_balance():
    assert buy_item(100, 50) == 50


def test_calculate_reward_returns_total_reward():
    assert calculate_purchase_reward(100, 50) == 15


def test_can_afford_returns_false_when_balance_is_lower_then_price():
    assert can_afford(49, 50) == False


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

