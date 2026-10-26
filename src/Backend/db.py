import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine

load_dotenv()

url = URL.create(
    "mysql+pymysql",
    username=os.environ["pharma_user"],
    password=os.environ["STUDENT"],
    host=os.environ["localhost"],
    port=int(os.environ["3306"]),
    database=os.environ["pharma_ai"],
)

engine = create_engine(url, pool_pre_ping=True)