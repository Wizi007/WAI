#import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def check_word(string):
    try:
        string = string.replace(' ', '+')
        html = urlopen('https://en.wikipedia.org/wiki/' + string)
        bsObj = BeautifulSoup(html.read(),features="html.parser");
        return (bsObj.p)
    except:
        return('No internet connection')
        
def google_search(string):
    pass
