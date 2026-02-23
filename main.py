# main.py
# Chuong trinh quan ly kho POLY-LAP

from product_manager import *

def main():
    products = load_data()

    while True:
        print("1. Them san pham")
        print("2. Cap nhat san pham")
        print("3. Xoa san pham")
        print("4. Tim san pham")
        print("5. Hien thi tat ca")
        print("0. Thoat")

        choice = input("Chon: ")

        if choice == "1":
            add_product(products)
        elif choice == "2":
            update_product(products)
        elif choice == "3":
            delete_product(products)
        elif choice == "4":
            search_product_by_name(products)
        elif choice == "5":
            display_all_products(products)
        elif choice == "0":
            save_data(products)
            break

if __name__ == "__main__":
    main()
