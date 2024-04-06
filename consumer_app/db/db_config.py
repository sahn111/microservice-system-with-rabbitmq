from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv("POSTGRE_USER")
password = os.getenv("POSTGRE_PASSWORD")
url = os.getenv("POSTGRE_URL")
port = os.getenv("POSTGRE_PORT")
dbname = os.getenv("POSTGRE_DBNAME")

connection_url = f"postgresql://{user_name}:{password}@{url}/{dbname}"
sqlalchemy_engine = create_engine(connection_url)