from flask import Flask, jsonify
from flask_cors import CORS
import requests, urllib3, re
from html import unescape

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
CORS(app)

def get_info_posts(per_page=20, page=1):
    url = "https://www.srbvoz.rs/wp-json/wp/v2/info_post"
    params = {"per_page": per_page, "page": page}
    resp = requests.get(url, params=params, verify=False)
    if resp.status_code != 200:
        print("Greška HTTP:", resp.status_code, resp.text)
        return None
    return resp.json()

def extract_bg_voz_posts():
    posts = get_info_posts(per_page=10)
    results = []

    if not posts:
        return results

    for p in posts:
        title = p.get("title", {}).get("rendered", "")

        if "BG:VOZ" not in title:
            continue

        post_id = p.get("id")
        link = p.get("link", "")
        date = p.get("date", "")
        html_text = p.get("content", {}).get("rendered", "")
        text = re.sub(r'<.*?>', '', html_text)
        text = unescape(text).strip()

        formatted_date = None
        if date:
            date_part, time_part = date.split("T")
            yyyy, mm, dd = date_part.split("-")
            hh, minute, _ = time_part.split(":")
            formatted_date = f"{dd}.{mm}.{yyyy} - {hh}:{minute}"

        results.append({
            "id": post_id,
            "title": title,
            "date": formatted_date,
            "text": text,
            "link": link
        })

    return results

@app.route("/bgvoz")
def bgvoz():
    return jsonify(extract_bg_voz_posts())

@app.route("/")
def home():
    return jsonify({"message": "BG:VOZ backend, idite na /bgvoz za json."})

if __name__ == "__main__":
    app.run(debug=True)
