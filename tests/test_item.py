"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
@pytest.fixture()
def item():
    return Item("Яблоко", 2, 3)

def test_Item_init(item):
    assert item.name == "Яблоко"
    assert item.price == 2
    assert item.quantity == 3

def test_Item_calculate_total_price(item):
    assert item.calculate_total_price() == 6

def test_apply_discount(item):
    assert item.apply_discount() == 2
