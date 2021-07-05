
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from random import randint, choice
from time import sleep


driver = webdriver.Chrome("C:\\webdrivers\\chromedriver.exe")

query = "some interesting page.ru"
driver.get(query)

# enter
query = driver.find_element_by_class_name('form-control')
button = driver.find_element_by_class_name("bnt-enter")
query.send_keys('VZH8T8B5140')
button.click()

# first slide that requires to enter age and choose sex
age_query = driver.find_element_by_class_name("form-control")
sex_button = driver.find_element_by_class_name("sex-rbx")
continue_button = driver.find_element_by_class_name("btn")

age_query.send_keys(str(randint(18, 19)))
sex_button.click()
continue_button.click()

# starting test
start_test_button = driver.find_element_by_class_name("start_test")
start_test_button.click()

# begin test
html_list = driver.find_element_by_class_name("answers")
selection_options = html_list.find_elements_by_tag_name("button")
selection_options = selection_options[0:len(selection_options) - 3:]

for current_question in range(140):
    print(current_question)
    current_answer = choice(selection_options)
    print(current_answer.text)
    current_answer.click()
    continue_button = driver.find_element_by_class_name("answ-btn-next")
    continue_button.click()

    sleep(randint(5, 10))




