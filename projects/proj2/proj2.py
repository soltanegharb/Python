#Write a code to get the titles, views and tags of 1000 Continuous news and export it in a csv file.

"""
Our strategy:

    1st install requests, bs4
    
    2nd import requests, BeautifulSoup from bs4, csv
    
    3rd ask user to input the starting ID for the NEW he/she wants.
    
    4th get the page.
    
    5th make a for loop for 1000 pages.
    
    6th use BeautifulSoup which is bsoup in our code And use it to get the content of that page.
    
    7th find the header : h1 with class "headline"
    
    8th find the views : div with class "news-info"
    
    9th some edit on the found object in 8th step, to get views by number
    
    10th find the tags at footer : div with class "tags tags-news
    
    11th find all tags in found object in 10th step
    
    12th write to a file
"""
import requests
import csv
from bs4 import BeautifulSoup as bsoup

id = 1979577

all_exported = []
file = open("proj2export.csv", "w",encoding="utf-8")
writer = csv.writer(file)
for page_number in range(id ,id+11):
    temp = []
    page = f"https://www.varzesh3.com/news/{page_number}"
    response = requests.get(page)
    content = bsoup(response.content,"html.parser")
    header = content.find("h1", class_="headline")
    header = header.get_text().replace("\u200c", "")
    data = content.find("div", class_="news-info")
    views = int(float(data.find_all("span")[2].get_text().split(" ")[0][:-1]) * 1000 )
    tagsnews = content.find("div", class_="tags tags-news")
    tags = tagsnews.find_all("span")
    
    all_exported.append(header)
    all_exported.append(views)
    for tag in tags:
        temp.append(tag.get_text())
    all_exported.append(temp)
writer.writerow(all_exported)

print(all_exported)
file.close()
