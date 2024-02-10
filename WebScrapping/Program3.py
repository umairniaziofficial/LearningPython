import requests
from bs4 import BeautifulSoup

authors = set()
base_url = "http://quotes.toscrape.com/page/{}/"

try:
    page_number = 1
    while True:
        result = requests.get(base_url.format(page_number))
        result.raise_for_status()
        soup = BeautifulSoup(result.text, "lxml")
        quote_div = soup.select(".quote")

        if not quote_div:
            print("Exiting Form Quote Div Ended")
            break

        for quote in quote_div:
            author = quote.select_one(".author").getText()
            authors.add(author)

        page_number += 1

except requests.exceptions.HTTPError as e:
    print(f"Error: {e}")

print(sorted(authors))
