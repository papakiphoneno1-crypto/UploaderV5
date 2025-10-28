#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23198884"))
API_HASH = environ.get("API_HASH", "97e3ffaab185b63e1f74bf1c41abdf08")
BOT_TOKEN = environ.get("BOT_TOKEN", "7952077492:AAHfBuE1z3DkLKslrp03kXrh3vIRHJ49Dyk")

OWNER = int(environ.get("OWNER", "8277579429"))
CREDIT = environ.get("CREDIT", "_ANONYMOUS_")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7952077492').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7952077492').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set



