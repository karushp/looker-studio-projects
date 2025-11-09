import csv
import random
from datetime import datetime, timedelta
from calendar import monthrange

# Define categories
categories = ['Electronics', 'Home Appliances', 'Fashion', 'Sports', 'Beauty', 'Toys']

# Define regions
regions = ['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka', 'Hokkaido', 'Kyoto']

# Define channels
channels = ['Amazon', 'Retail', 'Website', 'Mercari']

# Product ID to Category mapping
product_category_mapping = {
    'P001': 'Electronics',
    'P002': 'Home Appliances',
    'P003': 'Fashion',
    'P004': 'Sports',
    'P005': 'Beauty',
    'P006': 'Toys',
    'P007': 'Electronics',
    'P008': 'Fashion',
    'P009': 'Home Appliances',
    'P010': 'Beauty',
    'P011': 'Sports',
    'P012': 'Toys',
    'P013': 'Electronics',
    'P014': 'Fashion',
    'P015': 'Home Appliances',
    'P016': 'Beauty',
    'P017': 'Sports',
    'P018': 'Toys',
    'P019': 'Electronics',
    'P020': 'Fashion',
}

# Price ranges by category (min, max)
category_price_ranges = {
    'Electronics': (200.0, 600.0),
    'Home Appliances': (150.0, 400.0),
    'Fashion': (30.0, 100.0),
    'Sports': (50.0, 150.0),
    'Beauty': (20.0, 50.0),
    'Toys': (25.0, 60.0),
}

# Units sold ranges by category (min, max)
category_units_ranges = {
    'Electronics': (30, 80),
    'Home Appliances': (25, 90),
    'Fashion': (50, 200),
    'Sports': (40, 150),
    'Beauty': (100, 300),
    'Toys': (60, 180),
}


def generate_sales_data(year):
    """Generate sales data for a given year"""
    data = []
    product_ids = list(product_category_mapping.keys())
    
    for month in range(1, 13):
        # Determine number of records for this month (40-50)
        num_records = random.randint(40, 50)
        
        # Get number of days in the month
        _, num_days = monthrange(year, month)
        
        for _ in range(num_records):
            # Random date within the month
            day = random.randint(1, num_days)
            date = datetime(year, month, day).strftime('%Y-%m-%d')
            
            # Random product_id
            product_id = random.choice(product_ids)
            
            # Get category from mapping
            category = product_category_mapping[product_id]
            
            # Generate unit_price based on category range
            min_price, max_price = category_price_ranges[category]
            unit_price = round(random.uniform(min_price, max_price), 2)
            
            # Generate units_sold based on category range
            min_units, max_units = category_units_ranges[category]
            units_sold = random.randint(min_units, max_units)
            
            # Calculate value
            value = round(units_sold * unit_price, 2)
            
            # Random region and channel
            region = random.choice(regions)
            channel = random.choice(channels)
            
            data.append({
                'date': date,
                'product_id': product_id,
                'category': category,
                'units_sold': units_sold,
                'unit_price': unit_price,
                'value': value,
                'region': region,
                'channel': channel
            })
    
    # Sort by date
    data.sort(key=lambda x: x['date'])
    
    return data


def write_csv(data, filename):
    """Write data to CSV file"""
    fieldnames = ['date', 'product_id', 'category', 'units_sold', 'unit_price', 'value', 'region', 'channel']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Generated {filename} with {len(data)} records")


def main():
    # Set random seed for reproducibility (optional)
    random.seed(42)
    
    # Generate data for 2024
    print("Generating data for 2024...")
    data_2024 = generate_sales_data(2024)
    write_csv(data_2024, 'sales_2024.csv')
    
    # Generate data for 2025
    print("Generating data for 2025...")
    data_2025 = generate_sales_data(2025)
    write_csv(data_2025, 'sales_2025.csv')
    
    print("\nCSV files generated successfully!")


if __name__ == '__main__':
    main()

