# 🛒 Billing System (Python + PyQt5 + PostgreSQL)

A **Python-based desktop billing application** built using **PyQt5** for the GUI and **PostgreSQL** for the database.  
It allows users to **add products, store them in a database, generate bills, and save invoices.**  

---

## 📌 Features
✅ **Add & Store Products** in a PostgreSQL database  
✅ **Select Products & Add to Cart**  
✅ **Generate Bill** in a pop-up window  
✅ **Save Bill as a Text File (`generated_bill.txt`)**  
✅ **Multi-user LAN Access (via PostgreSQL)**  

---

## 🚀 Installation Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/billing-system.git
cd billing-system
2️⃣ Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
Activate it:

Windows: venv\Scripts\activate
Linux/Mac: source venv/bin/activate
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up PostgreSQL Database
Open pgAdmin and create a new database:

Database Name: billing_system
User: billing_user
Password: billing_pass
Run this SQL query in pgAdmin:

sql
Copy
Edit
CREATE DATABASE billing_system;
CREATE USER billing_user WITH ENCRYPTED PASSWORD 'billing_pass';
GRANT ALL PRIVILEGES ON DATABASE billing_system TO billing_user;
5️⃣ Update Database Connection (database.py)
Modify the connection URL in database.py if needed:

python
Copy
Edit
DATABASE_URL = "postgresql://billing_user:billing_pass@localhost/billing_system"
6️⃣ Run the Application
sh
Copy
Edit
python app.py
🎉 The GUI will launch, allowing you to add products, generate bills, and save invoices!

📸 Screenshots
<img src="screenshots/main_window.png" width="500"> <img src="screenshots/bill_window.png" width="500">
🔗 Contributing
Want to improve this project? Follow these steps:

Fork the repository
Create a new branch (git checkout -b feature-name)
Commit your changes (git commit -m "Added a new feature")
Push to the branch (git push origin feature-name)
Open a Pull Request
📄 License
This project is open-source and available under the MIT License.

👩‍💻 Author
Shruti
📧 Contact: [shrutishukla297@gmail.com]


