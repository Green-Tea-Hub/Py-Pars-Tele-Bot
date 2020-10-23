import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

VK_USERNAME = str(os.getenv("VK_USERNAME"))
VK_PASSWORD = str(os.getenv("VK_PASSWORD"))
VK_APP_TOKEN = str(os.getenv("VK_APP_TOKEN"))
VK_GROUP_TOKEN = str(os.getenv("VK_GROUP_TOKEN"))

admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
