import requests
import urllib3
from html import unescape
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_info_posts(per_page=20, page=1):
    url = "https://www.srbvoz.rs/wp-json/wp/v2/info_post"
    params = {"per_page": per_page, "page": page}
    resp = requests.get(url, params=params, verify=False)
    if resp.status_code != 200:
        print("Greška HTTP:", resp.status_code, resp.text)
        return None
    return resp.json()

posts = get_info_posts(per_page=10)
if posts:
    for p in posts:
        title = p.get("title", {}).get("rendered", "")
        
        if("BG:VOZ" in title):
            post_id = p.get("id")
            link = p.get("link", "")
            date = p.get("date", "")
            html_text = p.get("content", {}).get("rendered", "")
            text = re.sub(r'<.*?>', '', html_text)
            text = unescape(text).strip()

            if date:
                date_part, time_part = date.split("T")
                yyyy, mm, dd = date_part.split("-")
                hh, minute, _ = time_part.split(":")
                formatted_date = f"{dd}.{mm}.{yyyy} - {hh}:{minute}"

            print(f"ID: {post_id}")
            print(f"Naslov: {title}")
            print(f"Datum: {formatted_date}\n")
            print(f"Tekst: {text}")
            print(f"Link: {link}")
            print("-----")
        else:
            continue