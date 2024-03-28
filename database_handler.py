import json
import os
from typing import List


class DatabaseHandler:
    def __init__(self):
        self.db_file = "scraped_data.json"
        if not os.path.exists(self.db_file):
            with open(self.db_file, "w") as f:
                json.dump([], f)
        self.cache = {}

    def update_database(self, data: List[dict]) -> int:
        updated_count = 0
        with open(self.db_file, "r+") as f:
            db_data = json.load(f)
            for new_entry in data:
                existing_entry = self.cache.get(new_entry["product_title"])
                if existing_entry and existing_entry == new_entry["product_price"]:
                    continue
                else:
                    if existing_entry:
                        db_data.remove({"product_title": new_entry["product_title"], "product_price": existing_entry})
                    db_data.append(new_entry)
                    self.cache[new_entry["product_title"]] = new_entry["product_price"]
                    updated_count += 1
            f.seek(0)
            json.dump(db_data, f, indent=4)
            f.truncate()
        return updated_count
