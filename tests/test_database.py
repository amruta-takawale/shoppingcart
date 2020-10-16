import mysql.connector
import sys


sys.path.append('../config/')

from config.database import Database

if __name__ == '__main__':
  print("Testing database connection")
  
  db = Database()
  db.create_connection("test_cart")

  create_table_sql = '''CREATE TABLE IF NOT EXISTS item_prices(
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                code CHAR(30) NOT NULL,
                                price FLOAT,
                                currency CHAR(8),
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                );'''

  db.create_table(create_table_sql)

  print(db.add_price('apple', 1, 'EUR'))
  print(db.add_price('kiwi', 1.12, 'EUR'))
  print(db.add_price('orange', 2, 'EUR'))

  print(db.fetch_prices())

