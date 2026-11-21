"""Optional generator for synthetic restaurant order records."""
import random
from datetime import date, timedelta

def generate_sample_orders(count=50):
    """Return fictional sample orders for educational use."""
    random.seed(11)
    menu = [
        ("Veg Burger", "Burger", 120), ("Paneer Pizza", "Pizza", 280),
        ("Masala Dosa", "South Indian", 140), ("Cold Coffee", "Beverage", 100),
        ("White Sauce Pasta", "Pasta", 220), ("Brownie", "Dessert", 110)
    ]
    customers = ["Aarav", "Diya", "Kabir", "Meera", "Ishaan"]
    payments = ["UPI", "Cash", "Card"]
    orders = []
    for i in range(1, count + 1):
        item, category, price = random.choice(menu)
        quantity = random.randint(1, 4)
        orders.append({
            "order_id": f"G{i:03d}",
            "order_date": (date(2026, 1, 1) + timedelta(days=i-1)).isoformat(),
            "customer_name": random.choice(customers),
            "food_item": item,
            "category": category,
            "quantity": quantity,
            "unit_price": price,
            "total_amount": quantity * price,
            "payment_method": random.choice(payments),
            "order_status": "Completed",
            "table_number": random.randint(1, 15)
        })
    return orders
