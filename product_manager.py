# product_manager.py
# Xu ly du lieu san pham POLY-LAP

import json
import os

DATA_FILE = "products.json"
def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        f = open(DATA_FILE, "r", encoding="utf-8")
        data = json.load(f)
        f.close()
        return data
    except:
        return []

def save_data(products):
    f = open(DATA_FILE, "w", encoding="utf-8")
    json.dump(products, f, ensure_ascii=False, indent=4)
    f.close()

