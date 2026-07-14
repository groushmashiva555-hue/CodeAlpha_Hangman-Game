import csv

def track_portfolio():
    
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 410,
        "AMZN": 175
    }
    
    portfolio = []
    total_investment = 0.0

    print("--- Welcome to your Stock Portfolio Tracker ---")
    print("Available stocks and prices per share:")
    for ticker, price in stock_prices.items():
        print(f"  {ticker}: ${price}")
        
    print("\nEnter your holdings (type 'done' when finished):")
    
    
    while True:
        ticker = input("Enter stock ticker (e.g., AAPL): ").strip().upper()
        
        if ticker == 'DONE':
            break
            
        if ticker not in stock_prices:
            print(f"Sorry, {ticker} is not in our price list. Try again.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity of {ticker}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
        except ValueError:
            print("Please enter a valid integer for quantity.")
            continue
        
        price_per_share = stock_prices[ticker]
        stock_total_value = price_per_share * quantity
        total_investment += stock_total_value
        
        portfolio.append({
            "ticker": ticker,
            "quantity": quantity,
            "price": price_per_share,
            "total": stock_total_value
        })

    
    print("\n" + "="*40)
    print("PORTFOLIO SUMMARY")
    print("="*40)
    if not portfolio:
        print("No stocks added to portfolio.")
    else:
        for item in portfolio:
            print(f"{item['ticker']} | Qty: {item['quantity']} | Price: ${item['price']} | Value: ${item['total']}")
        print("-"*40)
        print(f"Total Investment Value: ${total_investment:.2f}")
        print("="*40)
        
        
        save_choice = input("Do you want to save this summary to a CSV file? (y/n): ").strip().lower()
        if save_choice == 'y':
            filename = "portfolio_summary.csv"
            try:
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Ticker", "Quantity", "Price Per Share", "Total Value"])
                    for item in portfolio:
                        writer.writerow([item["ticker"], item["quantity"], item["price"], item["total"]])
                    writer.writerow([])
                    writer.writerow(["Total Investment", "", "", total_investment])
                print(f"Portfolio successfully saved to {filename}!")
            except IOError:
                print("An error occurred while saving the file.")

if __name__ == "__main__":
    track_portfolio()
