from pathlib import Path
import pandas as pd

COLUMNS = [
    "order_id", "order_date", "customer_name", "food_item", "category",
    "quantity", "unit_price", "total_amount", "payment_method",
    "order_status", "table_number"
]

def load_orders(file_path):
    """Read restaurant orders from a CSV file and handle missing values."""
    path = Path(file_path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(columns=COLUMNS).to_csv(path, index=False)
        return []

    df = pd.read_csv(path)
    for column in ["customer_name", "food_item", "category", "payment_method", "order_status"]:
        if column in df.columns:
            df[column] = df[column].fillna("Unknown")
    for column in ["quantity", "unit_price", "total_amount", "table_number"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce").fillna(0)
    if "order_date" in df.columns:
        df["order_date"] = df["order_date"].fillna("")
    if "order_id" in df.columns:
        df["order_id"] = df["order_id"].fillna("")
    return df.reindex(columns=COLUMNS).to_dict(orient="records")

def save_orders(orders, file_path):
    """Save all restaurant order records to CSV."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(orders, columns=COLUMNS).to_csv(path, index=False)
