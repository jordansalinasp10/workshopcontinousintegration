from app.utils import calculate_total_cost

def test_calculate_total_cost_no_discounts():
    base = 100
    additional = 50
    total = calculate_total_cost(base, additional, group=False, special=False, premium=False)
    assert total == 150

def test_calculate_total_cost_group_discount():
    base = 100
    additional = 50
    total = calculate_total_cost(base, additional, group=True, special=False, premium=False)
    assert total == 150  # 150 - 10%

def test_calculate_total_cost_special_discount():
    base = 250
    additional = 200
    total = calculate_total_cost(base, additional, group=False, special=True, premium=False)
    assert total == 430  # (450 - 20)


def test_calculate_total_cost_premium_surcharge():
    base = 200
    additional = 100
    total = calculate_total_cost(base, additional, group=False, special=False, premium=True)
    assert total == 350  # (300 + 15%)
