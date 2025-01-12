import os
from sqlalchemy import create_engine, text
from pymongo import MongoClient
from dotenv import load_dotenv
from loguru import logger

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE = "5_logs/validate_data.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logger.add(LOG_FILE, level="INFO")

def fetch_postgres_row_count():
    """Fetch row count from PostgreSQL table."""
    try:
        db_url = os.getenv("POSTGRES_DB_URL")
        if not db_url:
            raise ValueError("POSTGRES_DB_URL is not set in environment variables.")
        
        engine = create_engine(db_url)
        logger.info("Connecting to PostgreSQL to fetch row count...")
        
        with engine.connect() as connection:
            result = connection.execute(text("SELECT COUNT(*) FROM test_table"))
            row_count = result.scalar()
        logger.info(f"PostgreSQL row count: {row_count}")
        return row_count

    except Exception as e:
        logger.error(f"Error fetching row count from PostgreSQL: {e}")
        raise

def fetch_mongodb_row_count():
    """Fetch row count from MongoDB collection."""
    try:
        mongo_url = os.getenv("MONGODB_URL")
        if not mongo_url:
            raise ValueError("MONGODB_URL is not set in environment variables.")
        
        client = MongoClient(mongo_url)
        db = client["test_database"]
        collection = db["test_table"]
        row_count = collection.count_documents({})
        logger.info(f"MongoDB row count: {row_count}")
        return row_count

    except Exception as e:
        logger.error(f"Error fetching row count from MongoDB: {e}")
        raise

def validate_data():
    """Validate data consistency between PostgreSQL and MongoDB."""
    try:
        postgres_count = fetch_postgres_row_count()
        mongodb_count = fetch_mongodb_row_count()

        if postgres_count == mongodb_count:
            logger.info("Validation successful: Row counts match.")
            print("Validation successful: Row counts match.")
        else:
            logger.warning("Validation failed: Row counts do not match.")
            print("Validation failed: Row counts do not match.")
            print(f"PostgreSQL rows: {postgres_count}, MongoDB rows: {mongodb_count}")

    except Exception as e:
        logger.error(f"Validation error: {e}")
        print(f"Validation error: {e}")

if __name__ == "__main__":
    validate_data()