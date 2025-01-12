import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from loguru import logger

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE = "5_logs/test_connection.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logger.add(LOG_FILE, level="INFO")

def test_postgres_connection():
    """Tests connection to PostgreSQL database."""
    try:
        # Get database URL from environment variables
        db_url = os.getenv("POSTGRES_DB_URL")
        if not db_url:
            raise ValueError("POSTGRES_DB_URL is not set in environment variables.")

        # Establish connection
        logger.info("Attempting to connect to PostgreSQL database...")
        engine = create_engine(db_url)
        connection = engine.connect()
        logger.info("Connection to PostgreSQL successful!")
        print("Connection to PostgreSQL successful!")
        connection.close()

    except Exception as e:
        logger.error(f"Failed to connect to PostgreSQL: {e}")
        print(f"Failed to connect to PostgreSQL: {e}")
        raise

if __name__ == "__main__":
    test_postgres_connection()