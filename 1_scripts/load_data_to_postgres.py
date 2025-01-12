import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from loguru import logger

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE = "5_logs/load_data_to_postgres.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logger.add(LOG_FILE, level="INFO")

def load_data_to_postgres(file_path):
    """Loads CSV data to a PostgreSQL table."""
    try:
        # Read data from CSV
        logger.info(f"Reading data from {file_path}.")
        data = pd.read_csv(file_path)

        # PostgreSQL connection
        db_url = os.getenv("POSTGRES_DB_URL")
        if not db_url:
            raise ValueError("Database URL not found in environment variables.")

        engine = create_engine(db_url)
        logger.info("Connecting to PostgreSQL database...")

        # Insert data into table
        table_name = "test_table"
        data.to_sql(table_name, engine, if_exists="append", index=False)
        logger.info(f"Data successfully loaded into {table_name}.")

        # Print summary
        print(f"Data loaded to PostgreSQL table: {table_name}")
        print(f"Number of rows loaded: {len(data)}")

    except Exception as e:
        logger.error(f"Error while loading data to PostgreSQL: {e}")
        print(f"Error while loading data to PostgreSQL: {e}")
        raise

if __name__ == "__main__":
    csv_file = "2_data/test_data.csv"
    load_data_to_postgres(csv_file)