# Restaurant Management & Analysis System

A menu-driven Python project for managing restaurant orders and analyzing sales.

## Setup
Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

Run the project from its root folder:

```bash
python main.py
```

## Dataset
`data/restaurant_orders.csv` contains 120 fictional sample orders for academic practice. It is not real restaurant/customer data.

## Modules
- `main.py`: terminal menu and application workflow
- `file_handler.py`: CSV loading, missing-value handling and saving
- `restaurant_operations.py`: add, display, search, update and delete orders
- `analysis.py`: NumPy and Pandas analysis and reports
- `data_generator.py`: optional synthetic data generator

## Implemented requirements
- Python data structures: list, tuple, set, dictionary and list methods
- User-defined functions
- NumPy 1D and 2D arrays, indexing, slicing and statistical functions
- Pandas DataFrame, CSV, filtering, sorting, GroupBy and missing values
- Statistical analysis with `describe()`
- CSV file handling and CRUD operations
- Category-wise, monthly and best-selling item reports
- VS Code terminal output

## Academic project note
This is a learning/demo application. Sales revenue is calculated from completed orders; cancelled orders are excluded from sales summaries.
