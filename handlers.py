from aiogram import Dispatcher, F
from aiogram.types import Message
from config import TIKTOK_LINK_PATTERN, HEADERS
from utils import extract_media_urls
from downloader import download_and_send_media

def register_handlers(dp: Dispatcher):
    @dp.message(F.text.regexp(TIKTOK_LINK_PATTERN))
    async def tiktok_handler(message: Message):
        tiktok_url = message.text.strip()
        await message.reply("Downloading...")
        video_url, photo_urls = extract_media_urls(tiktok_url, HEADERS)
        if not video_url and not photo_urls:
            await message.reply("Cannot find media")
            return
        await download_and_send_media(video_url, photo_urls, message, HEADERS)

    @dp.message()
    async def fallback_handler(message: Message):
        await message.reply("Send a TikTok link")