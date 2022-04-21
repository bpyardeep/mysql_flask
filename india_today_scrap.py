from bs4 import BeautifulSoup
from flask import jsonify
import requests
import json



class India_Today_API:
    

    def __init__(self,genre,page) -> None:
        self.genre = genre
        self.page = page
        self.url = 'https://www.indiatoday.in/{}?page={}'.format(self.genre,self.page)
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text, 'html.parser')



    def get_article_list(self):
        article_list = []
        for i in self.soup.find_all("div", {"class": "catagory-listing"}):
            article_dict = {}
            article_dict['link'] = i.find('a')['href']
            article_dict['headline'] = i.find('h2')['title']
            article_dict['img_src'] = i.find('img')['src']
            if i.find('p') is None:
                article_dict['overview'] = ""
            else:
                article_dict['overview'] = i.find('p').text
            
            article_list.append(article_dict)
        return article_list

aL1 = India_Today_API("india",'0')
print(aL1.get_article_list())

page = 0

# Choose Genre {india, World, Business, coronavirus-covid-19-outbreak,trending-news}
genre = 'india'

url = 'https://www.indiatoday.in/{}?page={}'.format(genre,page)
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
article_list = []

for i in soup.find_all("div", {"class": "catagory-listing"}):
    article_dict = {}
    article_dict['link'] = i.find('a')['href']
    article_dict['headline'] = i.find('h2')['title']
    article_dict['img_src'] = i.find('img')['src']
    if i.find('p') is None:
        article_dict['overview'] = ""
    else:
        article_dict['overview'] = i.find('p').text
    
    article_list.append(article_dict)


#print((article_list))