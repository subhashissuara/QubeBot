from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import time
import requests
import json
import sys
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

#target = " " #Type your target's name here which is same as the contact name stored in your phone.
target = input("Type your target's name which is same as the contact name stored in your phone(and make sure it is correct):")

target_split = target.split()

if len(target_split) > 1:
    target_firstname = target_split[0]
else:
    target_firstname = target


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Press Enter after scanning the QR Code...')

try:
    TargetXML = driver.find_element_by_xpath('//span[@title = "{}"]'.format(target))
    TargetXML.click()
except:
    print("Target not found in recent chat! Quitting bot in 5... 4... 3... 2... 1...")
    time.sleep(5)
    sys.exit()



# Replies to messages
msg_to_hi1 = ("Greetings " + target_firstname + "! " + "I am Qube, a personal assistant. I am currently under development and can help you with the following commands:")
msg_to_hi2 = "-> .hi or .hello or .hey"   
msg_to_hi3 = "-> .what is my name?"
msg_to_hi4 = "-> .weather *city name*"
msg_to_hi5 = "-> .news"
msg_to_hi6 = "-> .bye or .see ya"
msg_to_hi7 = "Things to note:"    
msg_to_hi8 = "1. Make sure there is no gap between . and your command otherwise, you will be waiting for me and I won't know!"
msg_to_hi9 = "2. The commands are not case sensitive :)"
msg_to_whatismyname1 = "Hmmm..."
msg_to_whatismyname2 = ("It's " + target_firstname + "! How come you forgot your name huh?")
msg_to_bye1 = ("It was nice meeting you " + target_firstname + "!")
msg_to_bye2 = "See ya later!"

def SendStringMessage(msg):
    MsgBox = driver.find_elements_by_class_name('_1Plpp')
    MsgBox[0].send_keys(msg)
    SendButton = driver.find_elements_by_class_name('_35EW6')
    SendButton[0].click()

def getweather(cityname):
    api_key = '2580d00cea5b8a68bdb7c07a72f1ffbb'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + cityname
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"] - 273
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        msg_temp = ("Temperature (in celsius unit) -> " + str(current_temperature))
        msg_pressure = ("Atmospheric pressure (in hPa unit) -> " + str(current_pressure))
        msg_humidiy = ("Humidity (in percentage) = " + str(current_humidiy) + "%")
        msg_description = ("Condition: " + str(weather_description).capitalize())
        SendStringMessage(msg_temp)
        SendStringMessage(msg_pressure)
        SendStringMessage(msg_humidiy)
        SendStringMessage(msg_description)

    else:
        SendStringMessage("Oops...")
        SendStringMessage("City Not Found")

def news():
    News_URL = "https://news.google.com/news/rss"
    NewURLOpen = urlopen(News_URL)
    Xml_Page = NewURLOpen.read()
    NewURLOpen.close()
    Soup = soup(Xml_Page,"xml")
    Top_Stories = Soup.findAll("item")
    SendStringMessage("*Today's Top Stories...*")
    SendStringMessage("-"*31)
    for story in Top_Stories:
        SendStringMessage(story.title.text)
        #SendStringMessage("*Short Description*:")
        #SendStringMessage(story.description.text)
        SendStringMessage("*Link To Full Story:*")
        SendStringMessage(story.link.text)
        SendStringMessage(story.pubDate.text)
        #SendStringMessage("-"*58)

        
        
while True:
    try:
        MsgDiv = driver.find_elements_by_class_name('Tkt2p')
        MsgSpan = MsgDiv[0].find_elements_by_xpath('//span[@class = "selectable-text invisible-space copyable-text"]')
        SizeofMsgSpan = len(MsgSpan)
        LastMsgsReceivedList = []
        LastMsg = (MsgSpan[SizeofMsgSpan - 1].text).lower()
        SecondLastMsg = (MsgSpan[SizeofMsgSpan - 2].text).lower()
        LastMsgsReceivedList.append(SecondLastMsg)
        LastMsgsReceivedList.append(LastMsg)

        for i in range(len(LastMsgsReceivedList)):
            LastMsgReceivedSplit = LastMsgsReceivedList[i].split()
            if LastMsgReceivedSplit[0] == ".hi" or LastMsgReceivedSplit[0] == ".hello" or LastMsgReceivedSplit[0] == ".hey":
                SendStringMessage(msg_to_hi1)
                SendStringMessage(msg_to_hi2)
                SendStringMessage(msg_to_hi3)
                SendStringMessage(msg_to_hi4)
                SendStringMessage(msg_to_hi5)
                SendStringMessage(msg_to_hi6)
                SendStringMessage(msg_to_hi7)
                SendStringMessage(msg_to_hi8)
                SendStringMessage(msg_to_hi9)

            elif LastMsgReceivedSplit[0] == ".weather":
                if len(LastMsgReceivedSplit) > 2:
                    WholeCityName = [" ".join(LastMsgReceivedSplit[1:len(LastMsgReceivedSplit)])]
                    getweather(WholeCityName[0])
                else:
                    getweather(LastMsgReceivedSplit[1])
            
            elif LastMsgReceivedSplit[0] == ".news":
                news()

            elif LastMsgsReceivedList[i] == ".what is my name?" or LastMsgsReceivedList[i] == ".what is my name":
                SendStringMessage(msg_to_whatismyname1)
                SendStringMessage(msg_to_whatismyname2)
            
            elif LastMsgsReceivedList[i] == ".bye" or LastMsgsReceivedList[i] == ".see ya":
                SendStringMessage(msg_to_bye1)
                SendStringMessage(msg_to_bye2)
        time.sleep(0.5)
    except:
        time.sleep(0.5)
        pass




