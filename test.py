import requests
from bs4 import BeautifulSoup
from selenium import webdriver

req = requests.get("https://sports.news.naver.com/index.nhn")
html = req.text  # requests로 불러온 response를 str로 저장.
soup = BeautifulSoup(html, 'html.parser')
#BeautifulSoup로 html소스(str형식)를 python이 읽을 수 있는 형식으로
#바꾸기 위해 python의 내장함수인 .parser을 사용해 soup변수에 저장
my_title = soup.select('h3 > a')  # bs(이하 BeautifulSoup)를 이용해 특정 태그의 값들을 찾는다.
#여기서 my_title은 list객체이다.

for title in my_title:
    print(title.text)  # 각 태그 안의 텍스트 출력
    print(title.get('href')+'\n')  # 각 태그의 속성을 가져오기 ex) href
