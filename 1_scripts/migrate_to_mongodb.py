import os
import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
from dotenv import load_dotenv
from loguru import logger

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE = "5_logs/migrate_to_mongodb.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logger.add(LOG_FILE, level="INFO")

def fetch_data_from_postgres():
    """Fetch data from PostgreSQL table."""
    try:
        # PostgreSQL connection
        db_url = os.getenv("POSTGRES_DB_URL")
        if not db_url:
            raise ValueError("Database URL not found in environment variables.")

        engine = create_engine(db_url)
        logger.info("Connecting to PostgreSQL...")
        
        # Fetch data
        query = "SELECT * FROM test_table"
        data = pd.read_sql(query, engine)
        logger.info(f"Fetched {len(data)} rows from PostgreSQL.")
        return data

    except Exception as e:
        logger.error(f"Error fetching data from PostgreSQL: {e}")
        raise

def insert_data_into_mongodb(data):
    """Insert data into MongoDB collection."""
    try:
        # MongoDB connection
        mongo_url = os.getenv("MONGODB_URL")
        if not mongo_url:
            raise ValueError("MongoDB URL not found in environment variables.")

        client = MongoClient(mongo_url)
        db = client["test_database"]
        collection = db["test_table"]
        
        # Insert data into MongoDB
        records = data.to_dict("records")
        result = collection.insert_many(records)
        logger.info(f"Inserted {len(result.inserted_ids)} rows into MongoDB.")
        print(f"Inserted {len(result.inserted_ids)} rows into MongoDB.")

    except Exception as e:
        logger.error(f"Error inserting data into MongoDB: {e}")
        raise

if __name__ == "__main__":
    try:
        # Fetch data from PostgreSQL
        postgres_data = fetch_data_from_postgres()

        # Insert data into MongoDB
        insert_data_into_mongodb(postgres_data)

    except Exception as e:
        logger.error(f"Migration failed: {e}")
        print(f"Migration failed: {e}")