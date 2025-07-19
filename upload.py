import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# PostgreSQL connection config
load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

# Create connection string
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')

# Load CSV file
df = pd.read_csv("data/output.csv")

# Upload to PostgreSQL 
df.to_sql("sport", engine, if_exists="replace", index=False)

print("Data successfully uploaded to PostgreSQL.")
