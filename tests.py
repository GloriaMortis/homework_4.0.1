from classes import Category, Products
import pytest


@pytest.fixture
def data_category():
    dic = {
        "name": "Телефон",
        "description": "Средство современного общения",
        "products": [
            {
                "name": "iPhone 13",
                "description": "Современный флагман",
                "price": 80000.0,
                "quantity": 5
            }]
    }

    return Category(dic["name"], dic["description"], dic["products"])


def test_category(data_category):
    assert data_category.name == "Телефон"
    assert data_category.description == "Средство современного общения"
    assert data_category.total_categories == 1
    assert data_category.total_unique_total_products == 1

