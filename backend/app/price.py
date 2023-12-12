from price_module import filter_wines_by_price

# List of CSV file names related to different types of wines
wines = ['Red.csv', 'Rose.csv', 'Sparkling.csv', 'White.csv']

# User input for the maximum and minimum price
price_max = float(input('Enter the maximum price: '))
price_min = float(input('Enter the minimum price: '))

# Call the function and print the results
result = filter_wines_by_price(wines, price_min, price_max)

print(result)