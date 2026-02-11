import requests
from bs4 import BeautifulSoup

def parse_recipe(html):
    """
    Parse through the HTML to get things like food names (title), the ingredients and directions 
    """
    soup = BeautifulSoup(html, 'html.parser')
    
    title_tag = soup.find('h1', class_='article-heading text-headline-400')
    title = title_tag.get_text()

    ingredients_bucket = soup.find('ul', class_='mm-recipes-structured-ingredients__list')
    ingredients = ingredients_bucket.find_all('li')
    ingredients_list = []
    for item in ingredients:
        text = item.get_text()
        ingredients_list.append(text)
    return {
        "title": title,
        "ingredients": ingredients_list
    }

def download_html(url):
    """
    Download the HTML from https://www.allrecipes.com/banana-bread-baked-oatmeal-recipe-11880277
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=headers)
        recipe_data = parse_recipe(response.text)
        print(recipe_data)
    except Exception as e:
        print(f"Error: {e}")

url = "https://www.allrecipes.com/banana-bread-baked-oatmeal-recipe-11880277"
download_html(url)