#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "2467"))
API_HASH = environ.get("API_HASH", "81fa8ed2585194bcd69167ae4")
BOT_TOKEN = environ.get("7225853:AAGJwoe4h0YBiVsNn8kXGZlPZaGa2E", "")
OWNER = int(environ.get("OWNER", "1077356338"))
CREDIT = environ.get("CREDIT", "HydraBot")
#AUTH_USER = os.environ.get('AUTH_USERS', '1077356338').split(',')
#AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
#if int(OWNER) not in AUTH_USERS:
  #  AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
