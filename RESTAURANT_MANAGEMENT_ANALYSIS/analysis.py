import numpy as np
import pandas as pd

def to_dataframe(orders):
    """Convert order dictionaries into a Pandas DataFrame."""
    df = pd.DataFrame(orders)
    if df.empty:
        return df
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    for column in ["quantity", "unit_price", "total_amount", "table_number"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    return df

def generate_sales_report(orders):
    """Generate the restaurant's overall sales summary."""
    df = to_dataframe(orders)
    if df.empty:
        print("No data available for the sales report.")
        return
    completed = df[df["order_status"].str.lower() == "completed"]
    cancelled = df[df["order_status"].str.lower() == "cancelled"]
    revenue = completed["total_amount"].sum()
    print("\\n========== RESTAURANT SALES SUMMARY ==========")
    print(f"Total orders             : {len(df)}")
    print(f"Completed orders         : {len(completed)}")
    print(f"Cancelled orders         : {len(cancelled)}")
    print(f"Total revenue            : Rs. {revenue:,.2f}")
    print(f"Average completed order  : Rs. {completed['total_amount'].mean():,.2f}")
    print(f"Highest order value      : Rs. {completed['total_amount'].max():,.2f}")
    print(f"Lowest order value       : Rs. {completed['total_amount'].min():,.2f}")
    print("\\nSelected rows and columns:")
    print(df[["order_id", "food_item", "quantity", "total_amount"]].head(5).to_string(index=False))
    print("\\nPandas statistical description:")
    print(df[["quantity", "unit_price", "total_amount"]].describe().round(2))

def category_analysis(orders):
    """Use GroupBy to calculate category-wise restaurant sales."""
    df = to_dataframe(orders)
    if df.empty:
        print("No data available.")
        return
    completed = df[df["order_status"].str.lower() == "completed"]
    report = completed.groupby("category")["total_amount"].agg(
        order_count="count", total_sales="sum", average_order_value="mean"
    ).reset_index().sort_values("total_sales", ascending=False)
    print("\\n========== CATEGORY-WISE SALES ==========")
    print(report.to_string(index=False, formatters={
        "total_sales": "{:,.2f}".format,
        "average_order_value": "{:,.2f}".format
    }))

def monthly_analysis(orders):
    """Filter valid dates, sort records and group revenue by month."""
    df = to_dataframe(orders)
    if df.empty:
        print("No data available.")
        return
    df = df.dropna(subset=["order_date"]).copy()
    df = df[df["order_status"].str.lower() == "completed"]
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    report = df.groupby("month")["total_amount"].agg(
        orders="count", revenue="sum", average_order="mean"
    ).sort_index()
    print("\\n========== MONTHLY REVENUE ANALYSIS ==========")
    print(report.round(2).to_string())

def numpy_analysis(orders):
    """Create NumPy arrays and calculate required statistical measures."""
    if not orders:
        print("No data available.")
        return
    amounts = np.array([float(o["total_amount"]) for o in orders], dtype=float)  # 1D array
    quantities = np.array([int(o["quantity"]) for o in orders], dtype=int)
    sales_data = np.column_stack((quantities, amounts))  # 2D array

    print("\\n========== NUMPY STATISTICAL ANALYSIS ==========")
    print("1D total amount array (first 10):", amounts[:10])
    print("2D array [quantity, total amount] (first 5 rows):\\n", sales_data[:5])
    print("Indexing - first order amount:", amounts[0])
    print("Slicing - order amounts 5 to 10:", amounts[4:10])
    print(f"Sum                  : Rs. {np.sum(amounts):,.2f}")
    print(f"Mean                 : Rs. {np.mean(amounts):,.2f}")
    print(f"Maximum              : Rs. {np.max(amounts):,.2f}")
    print(f"Minimum              : Rs. {np.min(amounts):,.2f}")
    print(f"Standard deviation   : Rs. {np.std(amounts):,.2f}")

def best_selling_items(orders):
    """Find popular food items using Pandas GroupBy."""
    df = to_dataframe(orders)
    if df.empty:
        print("No data available.")
        return
    completed = df[df["order_status"].str.lower() == "completed"]
    report = completed.groupby("food_item").agg(
        units_sold=("quantity", "sum"),
        revenue=("total_amount", "sum")
    ).sort_values("units_sold", ascending=False).head(10)
    print("\\n========== TOP 10 BEST-SELLING ITEMS ==========")
    print(report.to_string())

def demonstrate_data_structures(orders):
    """Demonstrate list, tuple, set, dictionary and list methods."""
    order_ids = [o["order_id"] for o in orders]                 # List
    first_order_tuple = tuple(orders[0].items()) if orders else ()  # Tuple
    categories = {o["category"] for o in orders}                 # Set
    first_order_dict = orders[0] if orders else {}               # Dictionary
    order_ids.sort()                                              # List method
    print("List sample:", order_ids[:5])
    print("Tuple sample:", first_order_tuple[:3])
    print("Unique categories (set):", categories)
    print("Dictionary sample:", first_order_dict)
    print("List methods used: append() and sort()")
