from sys import argv
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

def options(inputLine):
    commands = ["", "", "", "", "T"]
    index = 0
    for i in inputLine:
        if (inputLine == '-msg'):
            index = 1
        elif (inputLine == '-n'):
            index = 2
        elif (inputLine == '-id'):
            index = 3
        elif (inputLine == '-sm'):
            commands[4] = "F"
        else:
            commands[index] = i
    return commands

safemode = True

commands = options(argv)

main = commands[0]

if (main == "spam"):

    msg = commands[1]
    spams = int(commands[2])
    ind = int(commands[3])-1
    if (commands[4] == 'T'):
        safemode = True
    elif (commands[4] == 'F'):
        safemode = False
    
    if (spams == ""):
        print("You must insert a spam number")
    elif (spams < 1):
        print("Spams number must be greater than 0!")
    if (ind < 0):
        print("Indexes start from 1!")

    print(msg,spams,ind)
    input()
                
    browser = wb.Chrome("C:\\Users\\Francesco\\Desktop\\Code\\Web\\chromedriver")

    browser.get("https://web.whatsapp.com/")

    wait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_2wP_Y")))

    browser.find_element_by_xpath('//div[@class="_2wP_Y" and contains(@style,"translateY(%dpx);")]' %(ind*72)).click()
    #Trying to delete spammed message, now hovering the message to let the arrow appear
    
    #chats = browser.find_elements_by_xpath('//div[@class="_3_7SH _3DFk6 focusable-list-item"]')

    #for i in chats:
        #hover = ActionChains(browser).move_to_element(i)
        #hover.perform()
        #time.sleep(2)
    
    if (safemode == "T"): 
        print("PRESS ENTER TO SEND SPAM")
        input()

    for i in range(spams):
        print("Sending",msg)

        textFields = browser.find_elements_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')

        textFields[1].send_keys(msg)

        buttons = browser.find_elements_by_class_name('weEq5')

        buttons[1].click()

    print("Successfully sent %d spams, press enter to continue" % (spams))
    input()
    browser.close()
    
elif (main == "help"):
    print("COMMANDS:")
    print("spam | Starts spamming, check options below")
    print("help | Shows this screen")
    print()
    print("OPTIONS:")
    print("Mandatory:")
    print('-msg | The message to send, example: spam -msg My message')
    print("-n | The number of spams to send, example: spam -msg My message -n 5")
    print("Optional:")
    print("-id | The index of the chat you wanna spam to, starting from the top of your whatsapp chats, default is 1")
    print("-sm | Just type it to deactivate safe mode, which requires a confirm before sending the spam")

else:
    print("NOT A VALID COMMAND")

print()
