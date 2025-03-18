import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QMessageBox, QDialog, QTextEdit
from database import SessionLocal, Product

class BillingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Billing System")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.product_input = QLineEdit(self)
        self.product_input.setPlaceholderText("Enter Product Name")
        layout.addWidget(self.product_input)

        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Enter Price")
        layout.addWidget(self.price_input)

        self.add_button = QPushButton("Add Product")
        self.add_button.clicked.connect(self.add_product)
        layout.addWidget(self.add_button)

        self.products_dropdown = QComboBox(self)
        layout.addWidget(self.products_dropdown)

        self.cart_button = QPushButton("Add to Cart")
        self.cart_button.clicked.connect(self.add_to_cart)
        layout.addWidget(self.cart_button)

        self.bill_button = QPushButton("Generate Bill")
        self.bill_button.clicked.connect(self.generate_bill)
        layout.addWidget(self.bill_button)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.cart = []  # Cart to store selected products
        self.load_products()

    def add_product(self):
        name = self.product_input.text()
        price = self.price_input.text()

        if not name or not price:
            QMessageBox.warning(self, "Error", "All fields are required!")
            return

        session = SessionLocal()
        new_product = Product(name=name, price=float(price))
        session.add(new_product)
        session.commit()
        session.close()

        QMessageBox.information(self, "Success", "Product added successfully!")
        self.product_input.clear()
        self.price_input.clear()
        self.load_products()

    def load_products(self):
        session = SessionLocal()
        products = session.query(Product).all()
        session.close()

        self.products_dropdown.clear()
        for product in products:
            self.products_dropdown.addItem(f"{product.name} - ${product.price}", product.id)

    def add_to_cart(self):
        selected_index = self.products_dropdown.currentIndex()
        if selected_index == -1:
            QMessageBox.warning(self, "Error", "No product selected!")
            return

        selected_product = self.products_dropdown.currentText()
        product_name, product_price = selected_product.split(" - $")  # Split name & price

        self.cart.append({"name": product_name, "price": float(product_price)})

        QMessageBox.information(self, "Added to Cart", f"{product_name} added to cart!")

    def generate_bill(self):
        if not self.cart:
            QMessageBox.warning(self, "Error", "Cart is empty! Please add products.")
            return

        total_amount = sum(item["price"] for item in self.cart)
        bill_text = "===== BILL =====\n"
        for item in self.cart:
            bill_text += f"{item['name']} - ${item['price']:.2f}\n"
        bill_text += f"\nTotal: ${total_amount:.2f}"

        self.show_bill_window(bill_text)

        # Save bill to a text file
        with open("generated_bill.txt", "w") as f:
            f.write(bill_text)

        QMessageBox.information(self, "Saved", "Bill saved as generated_bill.txt")

    def show_bill_window(self, bill_text):
        bill_window = QDialog(self)
        bill_window.setWindowTitle("Generated Bill")
        bill_window.resize(300, 400)

        bill_display = QTextEdit(bill_window)
        bill_display.setPlainText(bill_text)
        bill_display.setReadOnly(True)
        bill_display.resize(280, 380)

        bill_window.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BillingApp()
    window.show()
    sys.exit(app.exec_())
