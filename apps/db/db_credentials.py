import os

from dotenv import load_dotenv

load_dotenv()
DB_LOGIN = os.getenv("DB_LOGIN")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DB_URL = f"postgresql+asyncpg://{DB_LOGIN}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}"
