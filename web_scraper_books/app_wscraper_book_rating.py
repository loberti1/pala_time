"""scrap books.toscrape.com to get books with rating > 4
this code is still working by 02-2025"""
import bs4, requests as re
url_init = 'https://books.toscrape.com/catalogue/page-{}.html'
titles_big_rating = []

#start search in first 50 pages
for page in range(1, 51):

    url_page = url_init.format(page)
    result = re.get(url_page)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    #select book class
    books = soup.select('.product_pod')

    #iterate through books
    for  book in books:

        #get 4 or 5 stars only
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:
            book_title = book.select('a')[1]['title']
            titles_big_rating.append(book_title)

#get the books
for t in titles_big_rating:
    print(t)