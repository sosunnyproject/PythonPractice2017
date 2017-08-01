from bs4 import BeautifulSoup
import requests
import re

def is_video(td):
    """it's a video if it has exactly one pricelabel, and if
    the stripped text inside that pricelabel starts with 'Video'"""
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and
            pricelabels[0].text.strip().startswith("Video"))

def book_info(article):
    """given a BeautifulSoup <td> Tag representing a book,
    extract the book's details and return a dict"""

    title = article.find("p", "title").a.text
    by_author = article.find('p', 'note').text
    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
    #isbn_link = td.find("div", "thumbheader").a.get("href")
    #isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0] isbn은 새로운 페이지 소스코드에 없어서 삭제
    date = article.find("p", "note date2").text.strip()

    return {
        "title": title.strip(),
        "authors": authors,
        #"isbn": isbn,
        "date" :re.sub("\s+","",date)
    }


from time import sleep


def scrape(num_pages=2):
    base_url = "https://ssearch.oreilly.com/?i=1;page=*;q=data&act=pg_"

    books = []

    for page_num in range(1, num_pages + 1):
        print ("souping page", page_num)
        url = "".join([a + str(page_num) for a in base_url.split("*")])
        soup = BeautifulSoup(requests.get(url).text, 'html5lib')

        for article in soup('article', 'result product-result'):
            if not is_video(article):
                books.append(book_info(article))

        # now be a good citizen and respect the robots.txt!
        sleep(5)

    return books

a = scrape()
print(a)
