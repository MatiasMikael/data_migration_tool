import pandas as pd
import random
import os
from datetime import datetime
from loguru import logger

# Configure logging
LOG_FILE = "5_logs/generate_test_data.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logger.add(LOG_FILE, level="INFO")

def generate_test_data(rows=1000):
    """Generates test data with the specified number of rows."""
    logger.info(f"Starting data generation for {rows} rows.")
    
    # Define columns
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    countries = ["USA", "Finland", "Germany", "Japan", "India"]
    categories = ["Electronics", "Clothing", "Books", "Toys", "Food"]

    data = {
        "id": [i for i in range(1, rows + 1)],
        "name": [random.choice(names) for _ in range(rows)],
        "country": [random.choice(countries) for _ in range(rows)],
        "category": [random.choice(categories) for _ in range(rows)],
        "purchase_amount": [round(random.uniform(10.0, 1000.0), 2) for _ in range(rows)],
        "purchase_date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(rows)],
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)
    logger.info("Data generation completed.")
    return df

if __name__ == "__main__":
    try:
        # Generate test data
        rows = 1000
        test_data = generate_test_data(rows)

        # Save to CSV
        output_file = "2_data/test_data.csv"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        test_data.to_csv(output_file, index=False)
        logger.info(f"Test data saved to {output_file}.")

        # Print summary
        print(f"Generated {rows} rows of test data.")
        print(f"Sample data:\n{test_data.head()}")

    except Exception as e:
        logger.error(f"Error during data generation: {e}")
        raise