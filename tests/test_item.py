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
    item.apply_discount()
    assert item.price == 2.0

def test_name(item):
    assert item.name == "Яблоко"

def test_setter_name():
    item.name = "колбаса"
    assert item.name == "колбаса"

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number("2") == 2

