from bs4 import BeautifulSoup
import requests

#http
url = "http://thefluffingtonpost.com"
r = requests.get(url)

#saving html code that is translated via BeautifulSoup package
cute = BeautifulSoup(r.content, "html5lib")

#headlins
#find the difference between 1-1, 1-2
#1-1
heads = cute.findAll("h3", {"class" : "fluff-post-title"})
#class is saved as list type
print("Headlines 1-1: ")
print(heads)
print("\n")

#findall doesn't work with .text, only find(single)
#print(heads.text)

#1-2
print("Headlines 1-2: ")
for head in heads:
    print(head.text)
print("\n")

#paragraphs
pmultiple = cute.findAll("p")

print("Paragraphs: ")
for psingle in pmultiple:
    print(psingle.text)
print("\n")

#tags
#1-1
div_tags = cute.findAll("div", {"class": "post-tags"})
print("Tags 1-1: ")
for t in div_tags:
    for aTag in t.findAll('a', href=True):
        tags = aTag.get('href')
        print(tags[37:])
print("\n")

#1-2
#using select method which takes a CSS selector, JQuery
for a in cute.select('div.post-tags a[href]'):
    tags = a['href']
    print(tags[37:])
