from bs4 import BeautifulSoup
import requests
from lxml import etree

class Scraper:
    def __init__(self):
        self.url = None

    def get_pullution_tehran(self):
        self.url = "https://airnow.tehran.ir/"
        html_content = requests.get(self.url).text
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.find(id = 'ContentPlaceHolder1_lblAqi3h').text

    def get_temp_tehran(self):
        url = "https://www.delgarm.com/weather/8/tehran"
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        dom = etree.HTML(str(soup))
        return(dom.xpath('/html/body/div[2]/div/section/div[1]/div[1]/div/div[1]/span')[0].text.replace("°", ""))



