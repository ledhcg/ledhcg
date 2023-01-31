import random
import requests
from bs4 import BeautifulSoup

def get_quote():

    URL_DEFAULT = "https://www.brainyquote.com/topics/success-quotes"

    # Pages from 1-16 (31.01.2023)
    page_number = random.randrange(1, 16, 1)
    # Quotes in a page from 1-67(max)
    quote_number = random.randrange(1, 67, 1)
    # Form id = "pos_x_y" - x = page_number, y = quote_number
    id_quote = 'pos_'+str(page_number)+'_'+str(quote_number)
    # if page_number = 1, set URL is default else set URL_x - x = page_number 
    URL = 1 == page_number and URL_DEFAULT or URL_DEFAULT+'_'+str(page_number)

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    # Check Quote not found 
    if soup.find(id=id_quote, attrs={"class": "m-ad-brick"}):
        print('Quote not found!')
        return get_quote()

    quote = soup.find(id=id_quote).find("a", attrs={"class": "b-qt"}).text.strip()
    author = soup.find(id=id_quote).find("a", attrs={"class": "bq-aut"}).text.strip()

    update_readme("README.md", quote, author)

def update_readme(file, quote, author):
    with open(file, "r") as f:
        content = f.readlines()
    for i, line in enumerate(content):
        if line.startswith("```html"):
            content[i+1] = f"\"{quote}\"\n"
            content[i+2] = f"<!-- {author} -->\n"
            break
    with open(file, "w") as f:
        f.writelines(content)

if __name__ == "__main__":
    get_quote()