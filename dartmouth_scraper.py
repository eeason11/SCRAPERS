import pandas as pd
import lxml.html as lh
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/ethan/local/bin/chromedriver_win32/chromedriver.exe')
url = 'http://oracle-www.dartmouth.edu/dart/groucho/timetable.main'
driver.get(url)

SA_button = driver.find_element_by_xpath('//input[@value="Subject Area(s)"]')
SA_button.click()

AT_button = driver.find_element_by_xpath('//input[@type="radio" and @id="allterms"]')
AT_button.click()

AS_button = driver.find_element_by_xpath('//input[@type="radio" and @id="allsubjects"]')
AS_button.click()

SfC_button = driver.find_element_by_xpath('//input[@type="submit" and @value="Search for Courses"]')
SfC_button.click()

Table_elem = driver.find_element_by_xpath('//div/table[@border="0" and @align="center"]').get_attribute('outerHTML')

df = pd.read_html(Table_elem)
print(df)