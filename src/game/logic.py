class ItemType:
    WEAPON = "weapon"
    ARMOR = "armor"
    CONSUMABLE = "consumable"
    SKIN = "skin"


VALID_ITEM_TYPES = {
    ItemType.WEAPON,
    ItemType.ARMOR,
    ItemType.CONSUMABLE,
    ItemType.SKIN,
}


def is_valid_item_type(item_type: str) -> bool:
    return item_type in VALID_ITEM_TYPES


def can_start_quest(player_level: int, required_level: int) -> bool:
    return player_level >= required_level


def can_purchase_item(balance: int, price: int) -> bool:
    return balance >= price


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
        raise ValueError("Bonus percent can't be negative")
    base_reward = price // 10
    bonus = base_reward * bonus_percent // 100
    total_reward = base_reward + bonus
    return total_reward
