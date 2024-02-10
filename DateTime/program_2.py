import requests
import bs4

baseUrl = "http://quotes.toscrape.com/"
result = requests.get(baseUrl)
soup = bs4.BeautifulSoup(result.text, "lxml")

# authors = []
# quotes = []
#
# quote_div = soup.select(".quote")
# for quote in quote_div:
#     q = quote.select(".text")[0].getText()
#     a = quote.select(".author")[0].getText()
#     authors.append(a)
#     quotes.append(q)
#
# print(quotes)
# print(authors)

tags = [tag.getText() for tag in soup.select(".tags-box .tag")]

for tag in tags:
    print(tag)
