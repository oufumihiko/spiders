from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def get_td_id(id, game_type=5): #判断id的取值范围
    row = int(id / game_type)
    col = id % game_type
    id = 'td' + str(row) + str(col)
    return id

browser = webdriver.Chrome(executable_path='./chromedriver.exe')
browser.get('https://www.zxgj.cn/g/shuerte')

#设置游戏类型
input_type = input("输入游戏类型：（5~9）") or 5
input_type = int(input_type)
game_type = Select(browser.find_element_by_id('fgnum'))
game_type.select_by_value(str(input_type))

#点击开始
start = browser.find_element_by_id('start')
start.click()

#获取方块中的内容
trlist = browser.find_element_by_xpath('//*[@id="shulte"]/table/tbody')
td_content = trlist.find_elements_by_tag_name("td")
sqr = [] #将值按顺序储存为list
for td in td_content:
    sqr.append(td.text)

#按索引顺序点击方块
for cub_no in range(1,(input_type ** 2 + 1)):
    id = sqr.index(str(cub_no))
    td_id = get_td_id(id,input_type)
    # print(td_id)
    btn = browser.find_element_by_id(td_id)
    btn.click()


time.sleep(5)
browser.quit()