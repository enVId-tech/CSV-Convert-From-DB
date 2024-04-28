import csv
import sqlite3

# Replace MAIN_DB with the name of the database(s) you want to export
MAIN_DB = ['stocktwits.db']

# Path to save CSV files (will not work if the folder does not exist)
CSV_PATH = './csv'

for db in range(len(MAIN_DB)):
    conn = sqlite3.connect(f'./db/{MAIN_DB[db]}')
    cursor = conn.cursor()

    print(
        "Tables:",
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table';").fetchall())

    tables = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';").fetchall()

    # Go through each table
    for table in tables:
        table = table[0]
        print("Table:", table)

        # Get all rows from the table
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        # Write to CSV
        with open(f'{CSV_PATH}/{table}.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([i[0] for i in cursor.description])
            writer.writerows(rows)

    conn.close()