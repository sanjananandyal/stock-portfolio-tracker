# Hardcoded stock price dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("Available Stocks:", list(stock_prices.keys()))

# Taking user input
n = int(input("How many different stocks you want to add: "))

for i in range(n):
    stock = input("Enter stock name (Example: AAPL): ").upper()
    
    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        portfolio[stock] = qty
    else:
        print("Stock not available in price list")

# Calculating total investment
print("\n---- Portfolio Summary ----")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    
    print(f"{stock} -> {qty} shares x ${price} = ${investment}")

print("Total Investment Value = $", total_investment)

# Optional File Save
save = input("Do you want to save result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            f.write(f"{stock}: {qty} shares = ${investment}\n")
        f.write(f"Total Investment = ${total_investment}")

    print("Saved in portfolio.txt")
