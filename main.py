
import requests
from bs4 import BeautifulSoup
URL='https://www.plasteurasia.com/katilimci-listesi'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

""" 
#Firma isimlerini çekmek için
sayfa = requests.get(URL,headers = headers)
içerik= BeautifulSoup(sayfa.content,'html.parser')


firma_ismi = içerik.find(id="companyName").get_text()
print(firma_ismi)
"""

""" 
#Firma Telefon numaralarını çekmek için
import re

for i in range(1, 20):
    # Web sitesine istek yapın
    url = f"https://www.plasteurasia.com/katilimci-listesi?page={i}"
    response = requests.get(url)


    soup = BeautifulSoup(response.text, "html.parser")


    a_tags = soup.find_all("a")


    for a_tag in a_tags:
        href = a_tag.get("href")
        if href and href.startswith("tel:") and href.startswith("tel:"):

            phone_number = re.sub(r'^tel:', '', href)
            print(phone_number)
"""


















