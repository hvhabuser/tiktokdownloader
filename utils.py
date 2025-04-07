from bs4 import BeautifulSoup
import requests
import logging

def extract_media_urls(tiktok_url: str, headers: dict) -> tuple[str | None, list[str]]:
    try:
        response = requests.post(
            "https://ssstik.io/abc?url=dl",
            headers=headers,
            data={"id": tiktok_url, "locale": "en", "tt": "123"},
            timeout=10
        )
        if response.status_code != 200:
            logging.warning(f"Bad response from ssstik.io: {response.status_code}")
            return None, []
        soup = BeautifulSoup(response.text, "html.parser")
        video_link = soup.find("a", class_="pure-button")
        if video_link and "href" in video_link.attrs:
            href = video_link["href"]
            video_url = "https://ssstik.io" + href if href.startswith("/") else href
            return video_url, []
        photo_div = soup.find("div", class_="image-cards")
        if photo_div:
            photo_urls = [img["src"] for img in photo_div.find_all("img") if "src" in img.attrs]
            return None, photo_urls
        return None, []
    except Exception as e:
        logging.exception("Error extracting media URLs")
        return None, []