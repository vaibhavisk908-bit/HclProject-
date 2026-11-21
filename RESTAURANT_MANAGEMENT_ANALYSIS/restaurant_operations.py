def get_next_order_id(orders):
    """Generate the next unique order ID."""
    numbers = [
        int(str(order["order_id"])[1:])
        for order in orders
        if str(order.get("order_id", "")).startswith("R")
        and str(order["order_id"])[1:].isdigit()
    ]
    return f"R{max(numbers, default=0) + 1:03d}"

def add_order(orders, order):
    """Validate and add a restaurant order."""
    if int(order["quantity"]) <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if float(order["unit_price"]) < 0:
        raise ValueError("Unit price cannot be negative.")
    order["total_amount"] = round(int(order["quantity"]) * float(order["unit_price"]), 2)
    orders.append(order)  # List method: append()
    return orders

def display_orders(orders):
    """Print all orders in a formatted terminal table."""
    if not orders:
        print("No restaurant orders found.")
        return
    print("-" * 126)
    print("{:<7} {:<12} {:<13} {:<22} {:<15} {:>5} {:>11} {:>12} {:<13}".format(
        "Order", "Date", "Customer", "Food Item", "Category",
        "Qty", "Unit Price", "Total (Rs.)", "Status"
    ))
    print("-" * 126)
    for o in orders:
        print("{:<7} {:<12} {:<13} {:<22} {:<15} {:>5} {:>11.2f} {:>12.2f} {:<13}".format(
            o["order_id"], o["order_date"], str(o["customer_name"])[:12],
            str(o["food_item"])[:21], str(o["category"])[:14],
            int(o["quantity"]), float(o["unit_price"]), float(o["total_amount"]),
            str(o["order_status"])[:12]
        ))
    print("-" * 126)
    print("Total orders:", len(orders))

def search_order(orders, order_id):
    """Search an order by its unique ID."""
    return next((o for o in orders if o["order_id"] == order_id), None)

def update_order(orders, order_id, field, value):
    """Update an order field and recalculate total when needed."""
    allowed = {
        "customer_name", "food_item", "category", "quantity",
        "unit_price", "payment_method", "order_status", "table_number"
    }
    if field not in allowed:
        return orders, False
    for order in orders:
        if order["order_id"] == order_id:
            if field == "quantity" and int(value) <= 0:
                raise ValueError("Quantity must be greater than zero.")
            if field == "unit_price" and float(value) < 0:
                raise ValueError("Unit price cannot be negative.")
            order[field] = value
            order["total_amount"] = round(
                int(order["quantity"]) * float(order["unit_price"]), 2
            )
            return orders, True
    return orders, False

def delete_order(orders, order_id):
    """Delete an order by ID."""
    for index, order in enumerate(orders):
        if order["order_id"] == order_id:
            del orders[index]
            return orders, True
    return orders, False
