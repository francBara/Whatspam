from sys import argv
from pathlib import Path
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os


#The class names of useful html divs and spans, they are often changed by Meta

MESSAGE_FIELD = 'fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv'
CONTACT = 'ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr'
SEARCH_FIELD = '_13NKt copyable-text selectable-text'

class SpamSession:
    def __init__(self, name, message, spams, delay):
        self.name = name
        self.message = message
        self.spams = spams
        self.delay = delay

    def spam(self):
        getContact(self.name).click()
        textField = browser.find_element(By.XPATH, "//div[@class='%s' and @data-tab='10']" %(MESSAGE_FIELD))

        if (self.delay > 0):
            delay = self.delay / 1000;
            textField.clear()
            textField.send_keys(spamSession.message)
            textField.send_keys(Keys.ENTER)
            for i in range(spamSession.spams):
                time.sleep(delay)
                textField.clear()
                textField.send_keys(spamSession.message)
                textField.send_keys(Keys.ENTER)

        else:
            for i in range(spamSession.spams):
                textField.clear()
                textField.send_keys(spamSession.message)
                textField.send_keys(Keys.ENTER)


def displayHelp():

    print("""
 __    __ _           _                             
/ / /\ \ \ |__   __ _| |_ ___ _ __   __ _ _ __ ___  
\ \/  \/ / '_ \ / _` | __/ __| '_ \ / _` | '_ ` _ \ 
 \  /\  /| | | | (_| | |_\__ \ |_) | (_| | | | | | |
  \/  \/ |_| |_|\__,_|\__|___/ .__/ \__,_|_| |_| |_|
                             |_|                    
""")
    print("Whatspam lets you send multiple messages at a time in Whatsapp.")
    print("Once started, it will open your browser and require you to scan the QR code")
    print("with your phone, after this the script will do the rest.")
    print()
    print("Currently supports Google Chrome, requires the chromedriver to be in the same directory\nof the script and to be the same version of your browser.")
    print()
    print("OPTIONS:")
    print('-msg | The message to send')
    print("-to | The name of the target")
    print("-n | The number of spams to send")
    print()
    print("Optional:")
    print("-d | The delay between each message in milliseconds")

def options(inputLine):
    name = ""
    message = ""
    spams = 0
    delay = 0

    for i in range(1, len(inputLine)):
        if (inputLine[i] == '-msg'):
            message = inputLine[i + 1]
        elif (inputLine[i] == '-n'):
            spams = int(inputLine[i + 1])
        elif (inputLine[i] == '-to'):
            name = inputLine[i + 1]
        elif (inputLine[i] == '-d'):
            delay = int(inputLine[i + 1])
        i += 1

    if (name == "" or message == "" or spams <= 0 or delay < 0):
        raise(Exception())

    return SpamSession(name, message, spams, delay)

def getContact(name):
    try:
        return browser.find_element(By.XPATH, "//span[@class='%s' and @title='%s']" %(CONTACT, name))
    except:
        return browser.find_element(By.XPATH, "//span[@class='%s' and contains(@title, '%s')]" %(CONTACT, name))



spamSession = None
try:
    spamSession = options(argv)
except:
    displayHelp()
    exit()

browser = wb.Chrome(executable_path = os.getcwd() + '/chromedriver.exe')

browser.get("https://web.whatsapp.com/")

#Wating the QR Code scan
wait(browser, 50).until(EC.presence_of_element_located((By.XPATH, "//span[@class='%s']" %(CONTACT))))


try:
    spamSession.spam()
except:
    searchBar = browser.find_element(By.XPATH, "//div[@class='%s' and @data-tab='3']" %(SEARCH_FIELD))
    searchBar.clear()
    searchBar.send_keys(spamSession.name)
    
    wait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//span[@class='%s']" %(CONTACT))))

    spamSession.spam()


print("All message sent, press ENTER to close the browser")
input()




