import requests
from aiogram.types import BufferedInputFile, InputMediaPhoto
import logging

async def download_and_send_media(video_url: str | None, photo_urls: list[str], message, headers: dict):
    try:
        if video_url:
            response = requests.get(video_url, headers=headers, timeout=15)
            if response.status_code == 200:
                video_data = response.content
                await message.reply_video(
                    video=BufferedInputFile(video_data, filename="tiktok.mp4"),
                    caption="Разработано devai.digital"
                )
            else:
                await message.reply(f"Cannot download video (code: {response.status_code})")
        elif photo_urls:
            media_group = []
            for url in photo_urls:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    photo_data = response.content
                    media_group.append(
                        InputMediaPhoto(media=BufferedInputFile(photo_data, filename="tiktok.jpg"))
                    )
            if media_group:
                await message.reply_media_group(media_group)
                await message.reply("Разработано devai.digital")
            else:
                await message.reply("⚠️ Не удалось скачать фотографии")
        else:
            await message.reply("⚠️ Медиа не найдено")
    except Exception as e:
        logging.exception("Error downloading media")
        await message.reply(f"⚠️ Ошибка: {str(e)}")