
from config.database import Database


def get_price(source: str, product_code: str) -> dict:
  db = Database()
  db.create_connection("test_cart")
  record = db.fetch_price_by_code(product_code)
  return record



