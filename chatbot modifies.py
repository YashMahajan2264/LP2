class StockMarketTradingSystem:
    def __init__(self):
        self.portfolio = {}

    def buy_stock(self, symbol, quantity):
        # Simulated logic for buying a stock
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Bought {quantity} shares of {symbol}")

    def sell_stock(self, symbol, quantity):
        # Simulated logic for selling a stock
        if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
            self.portfolio[symbol] -= quantity
            print(f"Sold {quantity} shares of {symbol}")
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
        else:
            print("Not enough shares to sell.")

    def show_portfolio(self):
        print("Portfolio:")
        for symbol, quantity in self.portfolio.items():
            print(f"{symbol}: {quantity} shares")


# Example usage
if __name__ == "__main__":
    trading_system = StockMarketTradingSystem()
    while True:
        print("\nOptions:")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. Show Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            symbol = input("Enter the symbol of the stock to buy: ")
            quantity = int(input("Enter the quantity of shares to buy: "))
            trading_system.buy_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter the symbol of the stock to sell: ")
            quantity = int(input("Enter the quantity of shares to sell: "))
            trading_system.sell_stock(symbol, quantity)
        elif choice == "3":
            trading_system.show_portfolio()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
