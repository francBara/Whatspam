from sys import argv
from pathlib import Path
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

def options(inputLine):
    commands = ["", "", "0", "", "0", "T"]
    index = 0
    option = 0
    for i in range(1,len(inputLine)):
        if (inputLine[i] == '-msg'):
            index = 1
            option = 0
        elif (inputLine[i] == '-n'):
            index = 2
            option = 0
        elif (inputLine[i] == '-to'):
            index = 3
            option = 0
        elif (inputLine[i] == '-id'):
            index = 4
            option = 0
        elif (inputLine[i] == '-sm'):
            commands[5] = "F"
            option = 0
        elif (option):
            commands[index] += " " + inputLine[i]
        else:
            commands[index] = inputLine[i]
            option = 1
    return commands

commands = options(argv)

main = commands[0]

while (main == ""):
    print("Insert a command, or type help")
    main = input()

if (main == "spam"):

    msg = commands[1]
    spams = int(commands[2])
    name = commands[3]
    index = int(commands[4])-1

    if (commands[5] == 'T'):
        safemode = True
    elif (commands[5] == 'F'):
        safemode = False
    while (spams < 1):
        print("Insert a spam number (it must be greater than 0)")
        spams = int(input())
    while (name == "" and index == -1):
        print("Insert the target name")
        name = input()
    while (msg == ""):
        print("Insert a message")
        msg = input()

    #CHANGE THIS VALUE TO SET YOUR BROWSER AND LOCATE YOUR WEBDRIVER (you can download the webdriver from the links at https://selenium-python.readthedocs.io/installation.html)
    #Currently using a Firefox webdriver located in /usr/bin
    browser = wb.Firefox()

    browser.get("https://web.whatsapp.com/")
    #Wating the QR Code scan
    wait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_2wP_Y")))
    try:
        if (name != ""):    
            browser.find_element_by_xpath('//span[@class="_1wjpf _3NFp9 _3FXB1" and @title="%s"]' %(name)).click()
        else:
            browser.find_element_by_xpath('//div[@class="_2wP_Y" and contains(@style,"translateY(%dpx);")]' %(ind*72)).click()
    except:
        print("Target not found")
    else: 
        if (safemode): 
            print("PRESS ENTER TO START SPAMMING")
            input()

        textFields = browser.find_elements_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
        buttons = browser.find_elements_by_class_name('weEq5')

        for i in range(spams):
            print("Sending",msg)
            textFields[1].send_keys(msg)
            buttons[1].click()

        print("Successfully sent %d spams" % (spams))
        browser.close()
    
elif (main == "help"):
    print("Whatsapp spammer lets you send multiple messages at a time in whatsapp")
    print("Once started, it will open your browser and require you to scan the QR code")
    print("with your phone, after this the script will do the rest")
    print()
    print("COMMANDS:")
    print("spam | Starts spamming, check options below")
    print("help | Shows this screen")
    print()
    print("OPTIONS:")
    print("Mandatory:")
    print('-msg | The message to send, example: spam -msg My message')
    print("-to | The name of the target")
    print("-id | As an alternative to the name, the index of the target, starting from the top of your chats")
    print("-n | The number of spams to send")
    print("Optional:")
    print("-sm | Just type it to deactivate safe mode, which requires a confirm before sending the spam")

else:
    print("Unknown command")

print()
