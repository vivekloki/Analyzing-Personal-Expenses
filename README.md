# Personal Expense Tracker

## Project Title:
**Analyzing Personal Expenses**

## Project Description:
This project simulates an expense tracker for an individual, generates realistic monthly expense data using the Faker library, and stores it in a SQL database. It also uses Streamlit to create a user-friendly web application that allows users to visualize their spending patterns and analyze their finances. The project covers expense categories like bills, groceries, subscriptions, and personal spending.

## Skills & Tools:
- **Python**: For data generation, processing, and SQL integration.
- **SQL**: For storing and querying the generated expense data.
- **Streamlit**: For creating an interactive web application to visualize and analyze the expenses.
- **Faker**: To simulate realistic expense data.

## Project Structure:
1. **Data Generation**: The `data_generation.py` script generates monthly expense data using the `Faker` library and stores it in a SQLite database.
2. **Expense Tracker App**: The `tracker_app.py` script is a Streamlit app that allows users to select a month, view data for that month, and visualize total spending by category.

## Features:
- **Data Generation**: Automatically generates expense data for each month and stores it in an SQLite database.
- **SQL Queries**: The generated data can be queried using SQL, and insights can be derived from it.
- **Streamlit Visualization**: Displays the expense data in a tabular format and visualizes spending trends using bar charts.

## Setup:
1. **Install Dependencies**:
    Run the following command to install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Data Generation Script**:
    To generate the expense data and store it in the SQLite database, run the `data_generation.py` script:
    ```bash
    python data_generation.py
    ```

3. **Run the Streamlit App**:
    To launch the Streamlit app and start visualizing the expenses:
    ```bash
    streamlit run tracker_app.py
    ```

## Database:
- The project uses an SQLite database (`expenses.db`), with separate tables for each month.
- Each table contains the following columns:
  - `id`: Primary key
  - `date`: Date of the expense
  - `category`: Category of the expense (e.g., Food, Transportation)
  - `payment_mode`: Payment method (Cash, Online)
  - `description`: Description of the expense
  - `amount_paid`: Amount paid for the expense
  - `cashback`: Cashback received (if any)

## Screenshots:

## License:
This project is open-source. You can use it for learning and modify it according to your needs.
