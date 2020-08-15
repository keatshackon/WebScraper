import requests
from bs4 import BeautifulSoup


"""ENTER THE URL """
url=input("Please Enter The Full Url like ::\n[https://en.wikipedia.org/wiki/Domain_Name_System] Of The Any Website==")

"""OPENING A FILE NAMED ScrapedData.txt"""

f1=open("ScrapedData.txt","w",encoding="UTF-8")

try:
    """FETCHING THE DATA FROM WEBSITE"""
    res=requests.get(url)             
    soup=BeautifulSoup(res.text,"html.parser")
    # print(soup)
    soup=str(soup)
    # print(type(soup))
    """WRITITNG INTO FILE"""
    f1.write(soup)
    print("\n\nSUCCESSFULLY SCRAPED THE  GIVEN URL!!")


except Exception as e:
    print("\n\n",e)
finally:
    f1.close()
