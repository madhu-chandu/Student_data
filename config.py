from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("MYSQLHOST")
port = os.getenv("MYSQLPORT")
user = os.getenv("MYSQLUSER")
password = os.getenv("MYSQLPASSWORD")
database = os.getenv("MYSQLDATABASE")

db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(db_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
