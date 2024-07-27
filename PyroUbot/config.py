import os

from dotenv import load_dotenv

load_dotenv(".env")

API_ID: int = os.getenv('API_ID', "20700254")
API_HASH: str = os.getenv('API_HASH', "846688376b2eed9f1971d14bb47c069c")

BOT_TOKEN = os.getenv('BOT_TOKEN', "6947100952:AAHP6MXF1RpNQoWaj_kp5sLSS_d9eS-StEg")

OWNER_ID = int(os.getenv('OWNER_ID', "1922468902"))

LOGS_MAKER_UBOT = int(os.getenv('LOGS_MAKER_UBOT', " -1002226179471"))

MAX_BOT = int(os.getenv('MAX_BOT', "50"))

RMBG_API = os.getenv("RMBG_API")

OPENAI_KEY = os.getenv("OPENAI_KEY")

MONGO_URL = os.getenv("mongodb+srv://ubot2:ubot2@cluster0.lwbshh5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
