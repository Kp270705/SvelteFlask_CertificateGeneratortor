import os
from dotenv import load_dotenv
from pathlib import Path

# Get root directory path (assuming this script is always run from root or you want absolute reference)
env_path = Path(__file__).resolve().parents[1] / '.env'
load_dotenv(dotenv_path=env_path)

# Access environment variables
password1 = os.getenv("PASSWORD1")  # for kpkpkunal2005@gmail.com 
password2 = os.getenv("PASSWORD2")  # for kp145419@gmail.com
password3 = os.getenv("PASSWORD3")  # for kunalpathak4774@gmail.com

