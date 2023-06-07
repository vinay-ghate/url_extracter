#importing required libraries
import requests
import bs4



url = input("Enter url with https:// : ")

site_data = requests.get(url)  #geting source code of url


def extract_links(url):
    site_data = requests.get(url)  #geting source code of url
    data = bs4.BeautifulSoup(site_data.text,"lxml")  #converting source code to easy form
    links =  data.find_all('a')       #selecting all a tags in website () they contains urls
    for link in links:
        print(link['href']) #from a tags printing urls i.e. in href tag


extract_links(url) #calling function

