import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


input_text = ""
repeat_num = 0

def send_text():  # repeat_num, input_text
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("https://asked.kr")
    driver.find_element_by_name('id').send_keys("josukjun")
    driver.find_element_by_name('pw').send_keys("sjsj5757") #\n으로도 가능!
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # click = soup.select('button') => click은 list형태이다.
    # print(click)  # str(click)[16:25] = login_btn
    # for title in click:
    #     print(title.text)  # 각 태그 안의 텍스트 출력
    driver.find_elements_by_class_name('login_btn')[0].click() # driver.find_elements_by_tag_name('button')[0].click() => 이걸로도 가능!
    for i in range(0, repeat_num):
        driver.find_element_by_name('content').send_keys(input_text)
        # html = driver.page_source
        # soup = BeautifulSoup(html, 'html.parser')
        # button_tags = soup.select('button')
        # print(button_tags) #여기서 index 3번이 질문하기 버튼의 태그이다
        click_btn = driver.find_elements_by_tag_name('button')[3]
        click_btn.click()
        time.sleep(2) #알람창 뜨는 시간까지 기다리는 시간
        driver.switch_to.alert.accept()
        time.sleep(1)
    Is = input()

print("입력할 말을 입력하세요")
input_text = input()
print("반복할 횟수를 입력하세요")
repeat_num = int(input())

send_text()

print("성공 및 종료")
