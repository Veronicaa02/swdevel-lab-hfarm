import pandas as pd

def filter_wines_by_price(wine_files, price_min, price_max):
    """
    Filter wines based on a specified price range.

    Parameters:
    - wine_files: List of CSV file names related to different types of wines.
    - price_min: Desired minimum price.
    - price_max: Desired maximum price.

    Returns:
    - Pandas DataFrame with names and prices of wines in the specified price range.
    """
    # DataFrame to store all data from CSV files
    all_wines = pd.DataFrame()

    # Concatenation of data from CSV files
    for wine_type in wine_files:
        all_wines = pd.concat([all_wines, pd.read_csv(wine_type)], ignore_index=True)

    # Select wines in the specified price range
    wines_chosen_price = all_wines[(all_wines["Price"] >= price_min) & (all_wines["Price"] <= price_max)]

    return wines_chosen_price[["Name", "Price"]]

# # Usage
# file_path_regpie = 'app/regpie-RifugiOpenDa_2296-all.csv'  # Update with your file path
# Update with your file path
# merged_data = cleancsv1(file_path_regpie, file_path_shelters)
# print(merged_data)