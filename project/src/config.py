import os
from dotenv import load_dotenv


def load_env():
    """Load environment variables from the .env file."""
    load_dotenv()


def get_key(key_name):
    """Return the value of an environment variable."""
    return os.getenv(key_name)