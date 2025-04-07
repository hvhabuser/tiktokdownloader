import logging
import re

logging.basicConfig(level=logging.INFO)

TOKEN = ""

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36"
    )
}

TIKTOK_LINK_PATTERN = re.compile(r"https?://(vt\.tiktok\.com|www\.tiktok\.com)/\S+")