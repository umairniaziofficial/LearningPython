import requests
import bs4

for i in range(1, 3):
    baseUrl = "https://books.toscrape.com/catalogue/page-{}.html"
    result = requests.get(baseUrl.format(i))
    if result.status_code == 200:
        soup = bs4.BeautifulSoup(result.text, 'lxml')

        books = soup.select(".product_pod")

        for book in books:
            if len(book.select(".star-rating.Two")) != 0:
                book_title = book.select('a')[1]['title']
                print(book_title)
    else:
        print("Failed To connect to the Server")
