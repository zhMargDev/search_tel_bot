import requests
from bs4 import BeautifulSoup

def search_by_text(text):
    url = 'https://www.google.com/search?q='
    text_arr = text.split(' ')
    # classname yuRUbf   a tag = yuRUbf child[0] child[0] child[0] href
    for url_text in text_arr:
        url += f'+{url_text}'
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup)
        # Find 5 divs with class "yuRUbf"
        yuRUbf_tags = soup.find(id="search")
        print(yuRUbf_tags)
        # Loop through each div
    else:
        print(f"Request failed. Status code: {response.status_code}")
    return text_arr