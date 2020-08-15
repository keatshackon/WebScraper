import requests
from bs4 import BeautifulSoup

url=input("Please Enter The Full Url like ::\n[https://www.wikipedia.com] Of The Any Website==")

try:
    r=res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    # print(soup)
    soup=str(soup)
    # print(type(soup))
    f=open("Scraped Data.html","w",encoding="UTF-8")
    f.write(soup)
    print("\n\nSUCCESSFULLY SCRAPED THE  GIVEN URL!!")

except Exception as e:
    print(e)
finally:
    f.close()
