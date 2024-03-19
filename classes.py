class Category:

    name: str
    description: str
    products: list
    total_categories = 0
    total_unique_total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.total_unique_total_products += len(self.products)

        Category.total_categories += 1


class Products:

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
