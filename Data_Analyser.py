import csv

# ---------- 1. Load sales data ----------
def load_sales(filename):
    """
    Loads sales data from a CSV file.
    filename: string, e.g., "sales.csv"
    Returns a list of dictionaries for each row.
    """
    sales = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales.append(row)
    return sales

# ---------- 2. Calculate revenue per product ----------
def calculate_revenue(sales):
    """
    Calculates total revenue per product.
    Returns a dictionary: {product_name: revenue}
    """
    revenue_per_product = {}
    for sale in sales:
        product = sale["Product"]
        units = int(sale["Units_Sold"])
        price = int(sale["Price"])
        revenue = units * price
        if product not in revenue_per_product:
            revenue_per_product[product] = 0
        revenue_per_product[product] += revenue
    return revenue_per_product

# ---------- 3. Find highest revenue product ----------
def find_best_product(revenue_data):
    """
    Finds the product with the highest revenue.
    Returns (best_product, highest_revenue)
    """
    best_product = ""
    highest_revenue = 0
    for product in revenue_data:
        if revenue_data[product] > highest_revenue:
            highest_revenue = revenue_data[product]
            best_product = product
    return best_product, highest_revenue

# ---------- Main Program ----------
if __name__ == "__main__":
    # Call load_sales with the actual CSV file name
    sales = load_sales("sales.csv")  # <-- matches your real CSV file
    
    revenues = calculate_revenue(sales)
    best_product, best_revenue = find_best_product(revenues)

    print("Total Revenue per Product\n")
    for product, revenue in revenues.items():
        print(f"{product}: ${revenue}")

    print("\nHighest Revenue Product:", best_product)
    print("Total Revenue:", sum(revenues.values()))