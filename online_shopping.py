class Product:
    def __init__(self,name,price,product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

product1 = Product("Iphone", 120000 , 141)
product2 = Product("Ipad",139000 , 44)
product3 = Product("Laptop",78000,53)
product4 = Product("Headphones",20000,5)

products = [product1,product2,product3,product4]

for product in products:
    print(product.name,product.price,product.product_id)

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def view_cart(self):
            for product in self.products:
                print(product.name,product.price)

    def remove_products(self,product):
         self.products.remove(product)

                
cart = Cart()

cart.add_product(product3)
cart.add_product(product1)


cart.view_cart()

cart.remove_products(product1)

print("After removing:")

cart.view_cart()

