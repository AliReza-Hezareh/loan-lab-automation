import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://souderbroder-loan-lab.lovable.app"
API_KEY = os.getenv("API_KEY")
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set in environment variables")


if not ADMIN_API_KEY:
    raise ValueError("ADMIN_API_KEY is not set")