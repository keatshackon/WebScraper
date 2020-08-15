import requests
from bs4 import BeautifulSoup
#
# res= requests.get('C:\\Users\\my\\Desktop\\lmthnnreal')
# s=res.text
# print(s)
# # file=open("main","w")
# # file.write(s)
# from urllib.request import urlopen
#
# with urlopen('file:///C:/Users/my/Desktop/lmthnnreal/index.html') as story:
    # s=[]
    # for line in story:
    #     line_word=line.decode('UTF-8').split()
    #     for j in line_word:
    #         s.append(j)
    # #print(story)
    # soup=BeautifulSoup(story,'html.parser')
    #
    # print(soup.body.contents)

# #
# s=[]
# res= requests.get('https://www.gita.edu.in')
# print(res.text,"\n KERATS DSL,DSLMFSDLMFSLFLSDFLSDN")
# soup=BeautifulSoup(res.text,'html.parser')
# print(soup)

res=requests.get("http://bputexam.in/studentsection/resultpublished/studentresult.aspx")
soup=BeautifulSoup(res.text,"html.parser")

print(soup.text)
