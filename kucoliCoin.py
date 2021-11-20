from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://coinmarketcap.com/exchanges/kucoin/')
names = list()
driver.execute_script("window.scrollTo(0, window.scrollY + 5000)")
# Render The Pge
for j in range(1, 9):
    for i in range(3):
        driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
        sleep(.5)
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div[1]/div/div[2]/div/div[3]/div[2]/button').click()

sleep(2)
driver.execute_script("document.documentElement.scrollTop = 500;")

sleep(2)
driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/div').click()
sleep(1)
driver.execute_script(
    """document.evaluate('//*[@id="tippy-3"]/div/div[1]/div/div/button[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();""")


for i in range(0,420):
    s = driver.find_element_by_xpath(
        f'//*[@id="__next"]/div[1]/div/div[2]/div/div[3]/div[1]/div/table/tbody/tr[{i}]/td[3]/div/a').get_attribute('innerHTML')
    names.append(s)


with open('kucoli-coin.txt', 'w', newline='\n') as f:
    for i in range(len(names)):
        f.writelines(f'{i+1}.{names[i]}\n')

    f.close()

driver.close()
