import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
API_TOKEN = os.getenv("API_TOKEN", "")
TIMEOUT = int(os.getenv("API_TIMEOUT", "5"))
