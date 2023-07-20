import os
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_NAME = os.environ["DB_NAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_PORT = int(os.environ["DB_PORT"])
DB_URL = "postgresql+psycopg2://%s:%s@%s:%d/%s" % (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME,
)
