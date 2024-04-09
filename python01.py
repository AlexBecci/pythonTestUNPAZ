class Product:
    def __init__(self, product_id, name, description, stock_quantity, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.price = price

class Sale:
    def __init__(self, sale_id, product_id, product_name, product_description, quantity_sold, unit_price):
        self.sale_id = sale_id
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.quantity_sold = quantity_sold
        self.unit_price = unit_price
        self.total_price = quantity_sold * unit_price

class SalesSystem:
    def __init__(self):
        self.products = []
        self.sales = []
        self.product_id_counter = 1
        self.sale_id_counter = 1

    def add_product(self, name, description, stock_quantity, price):
        product = Product(self.product_id_counter, name, description, stock_quantity, price)
        self.products.append(product)
        self.product_id_counter += 1
        print(f"Producto '{name}' agregado.")

    def sell_product(self, product_id, quantity_sold):
        product = next((p for p in self.products if p.product_id == product_id), None)
        if product:
            if product.stock_quantity >= quantity_sold:
                product.stock_quantity -= quantity_sold
                sale = Sale(self.sale_id_counter, product.product_id, product.name, product.description, quantity_sold, product.price)
                self.sales.append(sale)
                self.sale_id_counter += 1
                print(f"Venta de '{product.name}' realizada.")
            else:
                print(f"No hay suficiente stock de '{product.name}' para realizar la venta.")
        else:
            print("Producto no encontrado.")

    def list_all_sales(self):
        print("Ventas realizadas:")
        for sale in self.sales:
            print(f"ID: {sale.sale_id}, Producto: {sale.product_name}, Cantidad: {sale.quantity_sold}, Precio Unitario: ${sale.unit_price}, Precio Total: ${sale.total_price}")

    def show_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Agregar Producto")
            print("2. Realizar Venta")
            print("3. Listar Ventas")
            print("4. Salir")

            option = input("Ingrese el número de opción deseada: ")

            if option == "1":
                name = input("Ingrese el nombre del producto: ")
                description = input("Ingrese la descripción del producto: ")
                stock_quantity = int(input("Ingrese la cantidad en stock: "))
                price = float(input("Ingrese el precio del producto: "))
                self.add_product(name, description, stock_quantity, price)
            elif option == "2":
                product_id = int(input("Ingrese el ID del producto a vender: "))
                quantity_sold = int(input("Ingrese la cantidad vendida: "))
                self.sell_product(product_id, quantity_sold)
            elif option == "3":
                self.list_all_sales()
            elif option == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")

# Ejemplo de uso
system = SalesSystem()
system.show_menu()
