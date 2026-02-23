# product_manager.py
# Phien ban quan ly san pham
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

def generate_new_id(products):
    if len(products) == 0:
        return "LT01"

    last_id = products[-1]["id"]
    number = int(last_id[2:]) + 1

    if number < 10:
        return "LT0" + str(number)
    else:
        return "LT" + str(number)

def add_product(products):
    name = input("Ten san pham: ")
    brand = input("Thuong hieu: ")
    price = int(input("Gia: "))
    quantity = int(input("So luong: "))

    product = {
        "id": generate_new_id(products),
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    print("Da them san pham thanh cong!")

def update_product(products):
    pid = input("Nhap ID can sua: ")

    for p in products:
        if p["id"] == pid:
            p["name"] = input("Ten moi: ")
            p["brand"] = input("Thuong hieu moi: ")
            p["price"] = int(input("Gia moi: "))
            p["quantity"] = int(input("So luong moi: "))
            print("Cap nhat thanh cong!")
            return

    print("Khong the tim thay san pham!")


def delete_product(products):
    pid = input("Nhap ID can xoa: ")

    for p in products:
        if p["id"] == pid:
            products.remove(p)
            print("Da xoa san pham thanh cong!")
            return

    print("Khong tim thay san pham!")

def search_product_by_name(products):
    key = input("Nhap ten can tim: ").lower()
    found = False

    for p in products:
        if key in p["name"].lower():
            print(
                p["id"], "|",
                p["name"], "|",
                p["brand"], "|",
                p["price"], "|",
                p["quantity"]
            )
            found = True

    if not found:
        print("Khong tim thay san pham!")


def display_all_products(products):
    if len(products) == 0:
        print("Kho rong!")
        return

    for p in products:
        print(p["id"], p["name"], p["brand"], p["price"], p["quantity"])







