import urllib, urllib.parse, urllib.error
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
"""
urllib is a standard Python library (meaning you don’t have to install anything extra to run this example)
and contains functions for requesting data across the web, handling cookies, and even changing metadata such as 
headers and your user agent.urllib is a standard Python library (meaning you don’t have to install anything extra 
to run this example) and contains functions for requesting data across the web, handling cookies, and even changing 
metadata such as headers and your user agent."""


# Test 1: utiliser urlopen et Beautifulsoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())
bsobj = BeautifulSoup(html.read(), "html5lib")
print(bsobj.h1)  # h1 est dans bsObj.html.body.h1, c'est un header

# Exercice 1
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:  # HTTPError generic exception, dans le cas ou page not found
        return None
    try:
        bsobj = BeautifulSoup(html.read())
        title_result = bsobj.body.h1
    except AttributeError as e:  # Si le serveur est introuvable, html sera un None et html.read()
        # génère une AttributeError
        return None
    return title_result

def get_tags(url):
    # url = input('Enter - ') # in case you want interactive Python
    url = 'http://www.dr-chuck.com/page1.htm'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))


if __name__ == "__main__":

    # Exercice 1
    title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
    if title is None:
        print("Title could not be found")
    else:
        print(title)
