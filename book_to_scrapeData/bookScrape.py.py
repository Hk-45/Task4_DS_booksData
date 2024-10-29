import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

bUrl = 'https://books.toscrape.com/'

bHeaders = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

bResp = rq.get(url=bUrl, headers=bHeaders)
bSoup = BeautifulSoup(bResp.content,'html.parser')
books = bSoup.find_all('article', attrs={'class':'product_pod'})

book = []
for bookData in books:
  title = bookData.h3.a["title"]
  #title = header.find_all('title',attrs={'title'})
  price = bookData.find('p',attrs={'class':'price_color'}).text
  rating = bookData.find('p',attrs={'class':'star-rating'})['class'][1]

  bookData ={
    'Title': title,
    'Price': price,
    'Rating': rating
  }
  
  book.append(bookData)

  print('title=', title)
  print('price =', price)
  print('rating =', rating)

bookDataDf = pd.DataFrame(book)
bookDataDf.to_csv('BooksData.csv')




# for bookPrice in price:
#     print('bookPrice :',bookPrice.text)

# booksPrice = [ {'Price':bookPrice.text} for bookPrice in price]

# print('booksPrice',booksPrice)

# for bookRating in rating:
#     print('rating :',bookRating)

# booksRating =[{'rating':bookRating} for bookRating in rating]

# print('booksRating',booksRating)