import faker
import random
import sqlite3
from datetime import date, timedelta  # Ensure timedelta is imported

# Initialize Faker instance
fake = faker.Faker()

# Expense categories
categories = ['Food', 'Transportation', 'Bills', 'Groceries', 'Subscriptions', 'Personal Spending']
payment_modes = ['Cash', 'Online']

def generate_expense_data(month, year, records=100):
    expenses = []
    start_date = date(year, month, 1)
    if month == 12:
        end_date = date(year, month, 31)
    else:
        end_date = date(year, month + 1, 1) - timedelta(days=1)
    
    for _ in range(records):
        date_value = fake.date_between(start_date=start_date, end_date=end_date)
        category = random.choice(categories)
        payment_mode = random.choice(payment_modes)
        description = fake.sentence(nb_words=5)
        amount_paid = round(random.uniform(10.0, 500.0), 2)
        cashback = round(random.uniform(0.0, 10.0), 2)
        expenses.append((date_value, category, payment_mode, description, amount_paid, cashback))
    return expenses

def create_table(cursor, month):
    table_name = f"{month:02d}"  # Zero-padded month name
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS "{table_name}" (
            id INTEGER PRIMARY KEY,
            date TEXT,
            category TEXT,
            payment_mode TEXT,
            description TEXT,
            amount_paid REAL,
            cashback REAL
        )
    ''')

# Main script
def main():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    year = 2023
    for month in range(1, 13):
        expenses = generate_expense_data(month, year)
        create_table(cursor, month)
        cursor.executemany(f'''
            INSERT INTO "{month:02d}" (date, category, payment_mode, description, amount_paid, cashback)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', expenses)

    conn.commit()
    conn.close()
    print("Data generation complete.")

if __name__ == "__main__":
    main()
