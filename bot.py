from pyrogram import Client
from pyrogram.types import ChatJoinRequest
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("join-request-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_chat_join_request()
async def approve(client, request: ChatJoinRequest):
    await request.approve()
    print(f"Approved: {request.from_user.first_name}")

app.run()
