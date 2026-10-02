# Stock Portfolio Tracker
# Internship Task 2

import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

portfolio = {}

print("=" * 50)
print("STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} - ₹{price}")

print("\nEnter the stocks you want to buy.")
print("Type 'done' when you have finished.\n")

while True:
    stock = input("Enter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock symbol. Please try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print(f"{quantity} shares of {stock} added successfully.\n")

    except ValueError:
        print("Please enter a valid number.\n")


# Calculate total investment
total_investment = 0

print("\n" + "=" * 50)
print("             PORTFOLIO SUMMARY")
print("=" * 50)

print(f"{'Stock':<10}{'Quantity':<10}{'Price':<12}{'Value':<12}")
print("-" * 50)

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    value = quantity * price
    total_investment += value

    print(f"{stock:<10}{quantity:<10}₹{price:<11}₹{value:<11}")

print("-" * 50)
print(f"Total Investment: ₹{total_investment}")
print("=" * 50)


# Save result to a text file
with open("portfolio.txt", "w", encoding="utf-8") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 40 + "\n")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        value = quantity * price

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ₹{price} | Value: ₹{value}\n"
        )

    file.write("=" * 40 + "\n")
    file.write(f"Total Investment: ₹{total_investment}\n")

print("\nPortfolio report saved successfully to portfolio.txt")