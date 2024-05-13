import os
API_ID = int(os.getenv("20401009"))
API_HASH = os.getenv("6445b43e4af228532e84848d1bb2eb64")
BOT_TOKEN = os.getenv("6882280996:AAFHCrV0s8yep4LGtYBXxoQQWMDS4oVy0i0")
DATABASE_URL = os.getenv("https://songplayrobot-1-eha0.onrender.com")
OWNER_ID = list({int(x) for x in os.environ.get("6975923843", "").split()})
