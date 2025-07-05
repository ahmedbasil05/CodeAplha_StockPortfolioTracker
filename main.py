
import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3500,
    "MSFT": 320
}

def display_available_stocks():
    print("\nAvailable Stocks:")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock}: ${price}")

def get_user_portfolio():
    portfolio = {}
    print("\nEnter your stock holdings (type 'done' to finish):")
    while True:
        stock = input("Stock Symbol: ").upper()
        if stock == 'DONE':
            break
        if stock not in STOCK_PRICES:
            print(f"'{stock}' not found. Try one of: {', '.join(STOCK_PRICES)}")
            continue
        try:
            qty = int(input("Quantity: "))
            if qty <= 0:
                print("Quantity must be a positive number.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("Please enter a valid integer for quantity.")
    return portfolio

def calculate_investment(portfolio):
    total_value = 0
    summary = []
    print("\nPortfolio Summary:")
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * qty
        total_value += value
        summary.append((stock, qty, price, value))
        print(f"  {stock}: {qty} shares × ${price} = ${value}")
    print(f"\nTotal Investment Value: ${total_value}")
    return summary, total_value

def save_to_csv(summary, total_value):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
        for row in summary:
            writer.writerow(row)
        writer.writerow(["", "", "Total Investment", total_value])
    print(f"Portfolio saved as '{filename}'")

def main():
    print("==== Welcome to Stock Portfolio Tracker ====")
    display_available_stocks()
    portfolio = get_user_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    summary, total_value = calculate_investment(portfolio)

    choice = input("Do you want to export the portfolio as CSV? (yes/no): ").strip().lower()
    if choice == 'yes':
        save_to_csv(summary, total_value)

    print("Thank you for using the Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
