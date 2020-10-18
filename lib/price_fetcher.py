import json
from pathlib import Path

from config.database import Database


def get_price(source: str, product_code: str) -> dict:
  record = None
  if source == "db":
    db = Database()
    db.create_connection("test_cart")
    record = db.fetch_price_by_code(product_code)
  else:
    with open(str(Path(__file__).parent.parent) + "/config/item_prices.json") as json_file:
      data = json.load(json_file)
      for item in data['item_prices']['items']:
        if item["code"] == product_code:
          record = item

  return record



