from file_handler import load_orders, save_orders
from restaurant_operations import (
    add_order, display_orders, search_order, update_order,
    delete_order, get_next_order_id
)
from analysis import (
    generate_sales_report, category_analysis, monthly_analysis,
    numpy_analysis, demonstrate_data_structures, best_selling_items
)

DATA_FILE = "data/restaurant_orders.csv"

def show_menu():
    print("\n" + "=" * 52)
    print("       RESTAURANT MANAGEMENT & ANALYSIS SYSTEM")
    print("=" * 52)
    print("1. Add New Order")
    print("2. Display All Orders")
    print("3. Search Order")
    print("4. Update Order")
    print("5. Delete Order")
    print("6. Generate Sales Summary Report")
    print("7. Category-wise Sales Analysis")
    print("8. Monthly Revenue Analysis")
    print("9. NumPy Statistical Analysis")
    print("10. Best-Selling Food Items")
    print("11. Exit")
    print("=" * 52)

def main():
    orders = load_orders(DATA_FILE)
    print(f"Loaded {len(orders)} restaurant order records.")
    print("\nPython data structure demonstration:")
    demonstrate_data_structures(orders)

    while True:
        show_menu()
        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            try:
                quantity = int(input("Quantity: "))
                unit_price = float(input("Unit price (Rs.): "))
                order = {
                    "order_id": get_next_order_id(orders),
                    "order_date": input("Order date (YYYY-MM-DD): ").strip(),
                    "customer_name": input("Customer name: ").strip(),
                    "food_item": input("Food item: ").strip().title(),
                    "category": input("Category: ").strip().title(),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "total_amount": quantity * unit_price,
                    "payment_method": input("Payment method: ").strip().title(),
                    "order_status": "Completed",
                    "table_number": int(input("Table number: "))
                }
                orders = add_order(orders, order)
                print("Order added successfully. Order ID:", order["order_id"])
            except ValueError as error:
                print("Invalid input:", error)

        elif choice == "2":
            display_orders(orders)

        elif choice == "3":
            order_id = input("Enter Order ID: ").strip().upper()
            result = search_order(orders, order_id)
            if result:
                for key, value in result.items():
                    print(f"{key.replace('_', ' ').title():18}: {value}")
            else:
                print("Order not found.")

        elif choice == "4":
            order_id = input("Enter Order ID to update: ").strip().upper()
            field = input(
                "Field (customer_name/food_item/category/quantity/unit_price/"
                "payment_method/order_status/table_number): "
            ).strip()
            value = input("Enter new value: ").strip()
            try:
                if field in ("quantity", "table_number"):
                    value = int(value)
                elif field == "unit_price":
                    value = float(value)
                orders, updated = update_order(orders, order_id, field, value)
                print("Order updated." if updated else "Order or field not found.")
            except ValueError:
                print("Invalid numeric value.")

        elif choice == "5":
            order_id = input("Enter Order ID to delete: ").strip().upper()
            orders, deleted = delete_order(orders, order_id)
            print("Order deleted." if deleted else "Order not found.")

        elif choice == "6":
            generate_sales_report(orders)

        elif choice == "7":
            category_analysis(orders)

        elif choice == "8":
            monthly_analysis(orders)

        elif choice == "9":
            numpy_analysis(orders)

        elif choice == "10":
            best_selling_items(orders)

        elif choice == "11":
            save_orders(orders, DATA_FILE)
            print("All data saved. Thank you for using the system!")
            break

        else:
            print("Please enter a valid menu option.")

        save_orders(orders, DATA_FILE)

if __name__ == "__main__":