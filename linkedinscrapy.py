import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

writer = csv.writer(open('output.csv','w+',encoding = 'utf-8-sig', newline = ''))
writer.writerow(['Name','Position','Company','Education','Location','URL'])

driver = webdriver.Chrome('C://Users//Dell//Downloads//chromedriver')
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
           
username = driver.find_element_by_xpath('//*[@id="username"]')
username_input = input("Enter your Username Here:-")
username.send_keys(username_input)
sleep(0.5)
           
password = driver.find_element_by_xpath('//*[@id="password"]')
password_input = input("Enter your Password Here:-")
password.send_keys(password_input)
sleep(0.5)           
           
           
sign_in_button = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
sign_in_button.click()
sleep(5)                      

search_query = driver.find_element_by_name("q")
search_query.send_keys('site:linkedin.com/in AND "python developer" AND "london"')
search_query.send_keys(keys.RETURN)
sleep(5)

urls = driver.find_element_by_xpath('//*[@class = "r"]/aaa[@href]')
urls = [url.get_attribute('href') for url in urls]
sleep(5)


for url in urls:
    driver.get(url)
    sleep(2)
    
    sel = Selector(text = driver.page_source)
    
    name = sel.xpath('//*[@class = "inline t-24 t-black t-normal break-words"]/text()').extract_first().split()
    
    name = ' '.join(name)
    
    position = sel.xpath('//*[@class = "mt1 t-18 t-black t-normal"]/text()').extract_first().split()
    position = ' '.join(position)
    
    experience = sel.xpath('//*[@class = "pv-top-card-v3--experience-list"]')
    
    company = experience.xpath('./li[@data-control-name = "position_see_more"]//span/text()').extract_first()
    company = ' '.join(company.split()) if company else None
    
    education = experience.xpath('./li[@data-control-name = "education_see_more"]//span/text()').extract_first()
    education = ' '.join(education.split()) if education else None
    
    
    location = ' '.join(sel.xpath('//*[@class = "t-16 t-black t-normal inline-block"]/text()').extract_first().split())
    
    url = driver.current_url
    

    
writer.writerow([name,position,company,education,location,url])

# driver.quit()
