import mysql.connector

#Class handles DDL and DML
class Database():

  def _init_(self, host: str):
    self.cartdb = None
  
  def create_connection(self, db_name: str):
    try: 
      self.cartdb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
      )

      cartcursor = self.cartdb.cursor()
      cartcursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_name))
      cartcursor.execute("USE {}".format(db_name))

    except mysql.connector.Error as err:
      print("Not able to connect to Database: ", err)

  # def exit_connection():


  def create_table(self, create_table_sql: str):
    try:
      cartcursor = self.cartdb.cursor()
      cartcursor.execute(create_table_sql)
    except mysql.connector.Error as err:
      print("Not able to create table: ", err)


  def add_price(self, *data):
    sql = ("INSERT INTO item_prices (code, price, currency)" 
           " VALUES (%s, %s, %s)")
    cartcursor = self.cartdb.cursor()
    cartcursor.execute(sql, data)
    self.cartdb.commit()
    return cartcursor.lastrowid


  def fetch_prices(self):
    cartcursor = self.cartdb.cursor()
    cartcursor.execute("SELECT id, code, price, currency, created_at, updated_at FROM item_prices")
    return cartcursor.fetchall()

  def fetch_price_by_code(self, code):
    cartcursor = self.cartdb.cursor(dictionary=True)
    cartcursor.execute("SELECT id, code, price, currency, created_at, updated_at FROM item_prices WHERE code = '{}'".format(code))
    return cartcursor.fetchone()

if __name__ == '__main__':
  Database.create_connection()