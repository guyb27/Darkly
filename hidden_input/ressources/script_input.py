
#IMPORTANT NE PAS OUBLIER DE RAJOUTER geckodriver pour firefox DANS UN REP DE $PATH

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

browser.get('http://192.168.0.13:8080/')
#assert 'Yahoo' in browser.title

#elem = browser.find_element_by_id('user_login')
#elem.text = "gmadec"
#browser.execute_script("document.getElementByClassName('button special big').setAttribute('value', 'gmadec')")

time.sleep(1)
browser.execute_script("document.getElementById('banner').getElementsByTagName('ul')[0].getElementsByTagName('li')[0].getElementsByTagName('a')[0].style.border='thick solid white'")
time.sleep(1)
browser.execute_script("document.getElementById('banner').getElementsByTagName('ul')[0].getElementsByTagName('li')[0].getElementsByTagName('a')[0].text='Cliquez ici'")
time.sleep(1)
#elem = browser.find_element_by_id('banner')  # Find the search box
#elem[0]
browser.execute_script("document.getElementById('banner').getElementsByTagName('ul')[0].getElementsByTagName('li')[0].getElementsByTagName('a')[0].click()")

time.sleep(1)
browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[4].getElementsByTagName('td')[0].getElementsByTagName('a')[0].style.border='thick solid black'")
time.sleep(1)
browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[4].getElementsByTagName('td')[0].getElementsByTagName('a')[0].click()")
time.sleep(1)
browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('table')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[1].getElementsByTagName('td')[1].getElementsByTagName('form')[0].getElementsByTagName('input')[0].setAttribute('type', 'text')")
time.sleep(1)
browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('table')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[1].getElementsByTagName('td')[1].getElementsByTagName('form')[0].getElementsByTagName('input')[0].setAttribute('value', 'Fl4G')")
time.sleep(1)
browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('table')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[1].getElementsByTagName('td')[1].getElementsByTagName('form')[0].getElementsByTagName('input')[1].style.border='thick solid green'")
time.sleep(1)
browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('table')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[1].getElementsByTagName('td')[1].getElementsByTagName('form')[0].getElementsByTagName('input')[1].click()")

#####################Connect to intra.42.fr

#browser.get('https://signin.intra.42.fr/users/sign_in')
#browser.execute_script("document.getElementById('user_login').setAttribute('value', 'jecombe')")
#browser.execute_script("document.getElementById('user_password').setAttribute('value', 'ton_password')")
#elem = browser.find_element_by_name('commit')  # Find the search box
#elem.click()
#time.sleep(10)


time.sleep(10)
#elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()
