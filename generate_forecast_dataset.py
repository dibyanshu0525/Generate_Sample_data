import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# --- Configuration for Data Generation ---
NUM_ROWS = 5000000  # You can adjust the number of rows as needed

# --- Lists for categorical data ---
VERSIONS = ['CashUp', 'Forecast']
LOCAL_CURRENCY_CODES = ['CAD', 'USD']
BUSINESS_UNITS = ['Ice Cream', 'Home Care', 'Nutrition', 'Personal Care','Beauty and Wellbeing']
DATA_TYPES = ['allocated overlay', 'base', 'base adj', 'manual overlay']
SCENARIOS = ['2021ACT', '2022ACT', '2023ACT', '2024ACT'] + [f'2025MRF{i}' for i in range(1, 13)]
COUNTRIES = ['USA', 'Canada', 'Mexico', 'Brazil', 'UK', 'Germany', 'France', 'Australia', 'Japan', 'India']
PRODUCTS = [
    'Magnum Classic Bar', 'Cornetto Cone', 'Ben & Jerry’s Chocolate Fudge Brownie', 'Kwality Wall’s Cassata', 'Fruttare Mango Stick', 'Feast Choco Bar', 'Breyers Vanilla Tub', 'Paddle Pop Rainbow',
    'Surf Excel Matic Detergent Powder', 'Rin Bar', 'Domex Disinfectant Toilet Cleaner', 'Cif Cream Surface Cleaner', 'Comfort Fabric Conditioner', 'Vim Dishwash Liquid', 'Sunlight Detergent Powder', 'Wheel Detergent Bar',
    'Horlicks Classic Malt', 'Boost Energy Drink', 'Ensure Nutrition Powder', 'PediaSure', 'Protinex', 'Nestlé Everyday Dairy Whitener', 'Women\'s Horlicks', 'Amul Protein Buttermilk',
    'Dove Beauty Bar', 'Lifebuoy Handwash', 'Pears Pure & Gentle Soap', 'Lux Velvet Glow Body Wash', 'Rexona Roll-on Deodorant', 'Pepsodent Toothpaste', 'Closeup Everfresh Gel', 'Glow & Lovely Face Cream',
    'Lakmé 9 to 5 Primer + Matte Lipstick', 'Pond’s Age Miracle Cream', 'Simple Hydrating Light Moisturizer', 'TRESemmé Keratin Smooth Shampoo', 'Vaseline Intensive Care Lotion', 'Love Beauty and Planet Coconut Water Shampoo', 'Toni & Guy Volume Plumping Mousse', 'Ayush Anti Dandruff Shampoo'
]
CHANNEL_DESCRIPTIONS = [
    'Hypermarket', 'Supermarket', 'Horeca', 'E-commerce', 'Convenience Store',
    'Wholesale', 'Pharmacy', 'Specialty Store'
]

# --- Generate Customer Names ---
def generate_customer_name():
    first_names = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel']
    last_names = ['Solutions', 'Enterprises', 'Group', 'Partners', 'Innovations', 'Distributors']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# --- Generate Data ---
data = {
    'Version': np.random.choice(VERSIONS, NUM_ROWS),
    'date': [],
    'BMI': np.random.uniform(1000, 50000, NUM_ROWS).round(2),
    'Coupons': np.random.uniform(50, 5000, NUM_ROWS).round(2),
    'NSV': np.random.uniform(100000, 5000000, NUM_ROWS).round(2),
    'PBO': np.random.uniform(100, 10000, NUM_ROWS).round(2),
    'Slotting': np.random.uniform(500, 20000, NUM_ROWS).round(2),
    'Trade': np.random.uniform(1000, 50000, NUM_ROWS).round(2),
    'Turnover': np.random.uniform(200000, 10000000, NUM_ROWS).round(2),
    'UOP': np.random.uniform(10, 1000, NUM_ROWS).round(2),
    'Volumes': np.random.uniform(5000, 500000, NUM_ROWS).round(2),
    'LocalCurrencyCode': np.random.choice(LOCAL_CURRENCY_CODES, NUM_ROWS),
    'CustomerName': [generate_customer_name() for _ in range(NUM_ROWS)],
    'BusinessUnit': np.random.choice(BUSINESS_UNITS, NUM_ROWS),
    'Entity': np.random.randint(100, 999, NUM_ROWS),
    'DataType': np.random.choice(DATA_TYPES, NUM_ROWS),
    'Account': ['ACC' + str(random.randint(1000, 9999)) for _ in range(NUM_ROWS)], # Example account codes
    'ChannelDescription': np.random.choice(CHANNEL_DESCRIPTIONS, NUM_ROWS),
    'AcquisitionTO': np.random.uniform(10000, 1000000, NUM_ROWS).round(2),
    'DeflatedTO': np.random.uniform(5000, 500000, NUM_ROWS).round(2),
    'DisposalTO': np.random.uniform(100, 10000, NUM_ROWS).round(2),
    'GrossProfit': np.random.uniform(20000, 2000000, NUM_ROWS).round(2),
    'SupplychainCost': np.random.uniform(5000, 500000, NUM_ROWS).round(2),
    'Scenario': np.random.choice(SCENARIOS, NUM_ROWS),
    'Country': np.random.choice(COUNTRIES, NUM_ROWS),
    'Products': np.random.choice(PRODUCTS, NUM_ROWS)
}

# --- Generate Dates (2023, 2024, 2025) ---
start_date_2023 = datetime(2023, 1, 1)
end_date_2023 = datetime(2023, 12, 31)
start_date_2024 = datetime(2024, 1, 1)
end_date_2024 = datetime(2024, 12, 31)
start_date_2025 = datetime(2025, 1, 1)
end_date_2025 = datetime(2025, 12, 31)

for _ in range(NUM_ROWS):
    year_choice = random.choice([2023, 2024, 2025])
    if year_choice == 2023:
        random_date = start_date_2023 + timedelta(days=random.randint(0, (end_date_2023 - start_date_2023).days))
    elif year_choice == 2024:
        random_date = start_date_2024 + timedelta(days=random.randint(0, (end_date_2024 - start_date_2024).days))
    else: # 2025
        random_date = start_date_2025 + timedelta(days=random.randint(0, (end_date_2025 - start_date_2025).days))
    data['date'].append(random_date.strftime('%d/%m/%Y'))

# Create DataFrame
df = pd.DataFrame(data)

# Display a sample of the data
print("Generated Dataset Sample:")
print(df.head())

# Save to CSV
csv_file_name = 'sales_dataset.csv'
df.to_csv(csv_file_name, index=False)
print(f"\nDataset saved to '{csv_file_name}' with {NUM_ROWS} rows.")