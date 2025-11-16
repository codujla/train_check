# BG:VOZ News Scraper

Python script that fetches and displays train service updates about BG:VOZ using their public API.

## Requirements

- Python 3.10+
- requests
- urllib3

## Usage

1. Clone the repository:

```bash
git clone https://github.com/USERNAME/train_check.git
cd train_check
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python main.py
```

## Description

The script fetches the latest news/posts from [Srbija voz](https://srbijavoz.rs/) via their API and prints relevant information.

## Notes

The script disables SSL verification warnings due to certificate issues (verify=False in requests).

Adjust per_page in the script if you want to fetch more or fewer posts.

Added flask app for web page, also hosted [here](https://train-check-backend.onrender.com/bgvoz).

