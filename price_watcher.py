import csv


PRODUCT_DATA_CSV = "product_data.csv"
REPORT_CSV = "price_report.csv"

def track_prices(product_data_csv):
    # Read the product data from the CSV file
    with open(product_data_csv, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            title = row[0]
            amazon_price = float(row[2])  # Assuming price is in the third column
            flipkart_price = float(row[3])  # Assuming price is in the fourth column
            maple_price = float(row[4])  # Assuming price is in the fifth column

            # Track historical lowest prices for each e-commerce platform (you need to implement this logic)
            amazon_historical_lowest_price = 80000  # Example historical lowest price for Amazon
            flipkart_historical_lowest_price = 80000  # Example historical lowest price for Flipkart
            maple_historical_lowest_price = 80000  # Example historical lowest price for Maple
            print(amazon_price)

            # Compare current prices with historical lowest prices
            if amazon_price < amazon_historical_lowest_price:
                price_drop_percentage = ((amazon_historical_lowest_price - amazon_price) / amazon_historical_lowest_price) * 100
                print(f"Price dropped for {title} on Amazon! Previous lowest price: {amazon_historical_lowest_price}, Current price: {amazon_price}, Price drop: {price_drop_percentage:.2f}%")
                # You can calculate the percentage drop and include it in the message if needed

            if flipkart_price < flipkart_historical_lowest_price:
                price_drop_percentage = ((flipkart_historical_lowest_price - flipkart_price) / flipkart_historical_lowest_price) * 100
                print(f"Price dropped for {title} on Flipkart! Previous lowest price: {flipkart_historical_lowest_price}, Current price: {flipkart_price}, Price drop: {price_drop_percentage:.2f}%")

            if maple_price < maple_historical_lowest_price:
                price_drop_percentage = ((maple_historical_lowest_price - maple_price) / maple_historical_lowest_price) * 100
                print(f"Price dropped for {title} on Maple! Previous lowest price: {maple_historical_lowest_price}, Current price: {maple_price}, Price drop: {price_drop_percentage:.2f}%")

if __name__ == "__main__":
    track_prices(PRODUCT_DATA_CSV)