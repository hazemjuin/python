class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def sell_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                return product
# Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.id = 0

    def print_info(self):
        print(f"Product name: {self.name}")
        print(f"Product price: {self.price}")
        print(f"Product quantity: {self.quantity}")

    def update_price(self, new_price):
        self.price = new_price

    def __repr__(self):
        return f"<Product name={self.name} price={self.price} quantity={self.quantity}>"


def main():
    store = Store("My Store", "123 Main Street")
    product1 = Product("Apple", 1.00, 10)
    product2 = Product("Orange", 0.50, 20)

    store.add_product(product1)
    store.add_product(product2)

    print(store.products)

    # Sell the first product
    product = store.sell_product(product1.id)

    print(product)


if __name__ == "__main__":
    main()

