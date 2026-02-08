import requests
from bs4 import BeautifulSoup

def download_html(url):
    """
    Download the HTML from https://www.allrecipes.com/banana-bread-baked-oatmeal-recipe-11880277
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers)
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

url = "https://www.allrecipes.com/banana-bread-baked-oatmeal-recipe-11880277"
download_html(url)