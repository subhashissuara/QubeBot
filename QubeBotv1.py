# ------------------------
# QubeBot, a whatsapp bot.
# Writtern by QuantumBrute
# ------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import requests
import json
import sys
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# To get the target
Target = input("Type your Target's name which should be same as the contact name stored in your phone:")
Target.capitalize()

Target_Split = Target.split()

# To make the bot respond to author by first name only
if len(Target_Split) > 1:
    Target_Firstname = Target_Split[0]
else:
    Target_Firstname = Target

# Defines chrome as the webdriver and opens the whatsapp web link
Driver = webdriver.Chrome()
Driver.get('https://web.whatsapp.com/')

# Waits for any input to proceed further
input('Press Enter after scanning the QR Code...')

try:
    # Searches for target in recent chats
    Target_XML = Driver.find_element_by_xpath('//span[@title = "{}"]'.format(Target))
    Target_XML.click()  
except:
    try:
        # Searches for target in contact list
        Search_Bar = Driver.find_element_by_class_name('_2MSJr')
        Search_Bar.click()
        time.sleep(1)
        Search_Type = Search_Bar.find_element_by_xpath('//input[@class = "jN-F5 copyable-text selectable-text"]')
        Search_Type.send_keys(Target)
        time.sleep(2)
        Target_XML = Driver.find_element_by_xpath('//span[@title = "{}"]'.format(Target))
        Target_XML.click()
    except: 
        # If target is not found in any of the above cases   
        print("Target not found in contacts! Quitting bot in 5... 4... 3... 2... 1...")
        time.sleep(5)
        sys.exit()



# Replies for commands
Msg_For_Hi1 = ("Greetings " + Target_Firstname + "! " + "I am Qube, a personal assistant. I am currently under development and can help you with the following commands:")
Msg_For_Hi2 = "-> .hi or .hello or .hey"   
Msg_For_Hi3 = "-> .what is my name?"
Msg_For_Hi4 = "-> .weather *city name*"
Msg_For_Hi5 = "-> .news or .top stories"
Msg_For_Hi6 = "-> .bye or .see ya"
Msg_For_Hi7 = "Things to note:"    
Msg_For_Hi8 = "1. Make sure there is no gap between . and your command otherwise, you will be waiting for me and I won't know!"
Msg_For_Hi9 = "2. The commands are not case sensitive :)"
Msg_For_What_Is_My_Name1 = "Hmmm..."
Msg_For_What_Is_My_Name2 = ("It's " + Target_Firstname + "! How come you forgot your name huh?")
Msg_For_Bye1 = ("It was nice meeting you " + Target_Firstname + "!")
Msg_For_Bye2 = "See ya later!"

# Function to send messages in selected chat
def SendStringMessage(Msg):
    Msg_Box = Driver.find_elements_by_class_name('_1Plpp')
    Msg_Box[0].send_keys(Msg)
    Send_Button = Driver.find_elements_by_class_name('_35EW6')
    Send_Button[0].click()

# Function to get and reply weather of city requested
def getweather(City_Name):
    Api_key = '2580d00cea5b8a68bdb7c07a72f1ffbb'
    Base_url = "http://api.openweathermap.org/data/2.5/weather?"
    Complete_url = Base_url + "appid=" + Api_key + "&q=" + City_Name
    Response = requests.get(Complete_url)
    Response_JSON = Response.json()
    if Response_JSON["cod"] != "404":
        Response_JSON_Main = Response_JSON["main"]
        Current_Temperature = round((Response_JSON_Main["temp"] - 273.15),2)
        Current_Pressure = Response_JSON_Main["pressure"]
        Current_Humidiy = Response_JSON_Main["humidity"]
        Weather = Response_JSON["weather"]
        Weather_Description = Weather[0]["description"]
        Msg_Temp = ("Temperature -> " + str(Current_Temperature) +"°C")
        Msg_Pressure = ("Atmospheric pressure -> " + str(Current_Pressure) + " mbar")
        Msg_Humidiy = ("Humidity -> " + str(Current_Humidiy) + "%")
        Msg_Description = ("Condition: " + str(Weather_Description).capitalize())
        SendStringMessage(Msg_Temp)
        SendStringMessage(Msg_Pressure)
        SendStringMessage(Msg_Humidiy)
        SendStringMessage(Msg_Description)

    else:
        SendStringMessage("Oops...")
        SendStringMessage("City Not Found")

# Function to scrape and reply the top stories of the day
def news():
    News_URL = "https://news.google.com/news/rss"
    New_URL_Open = urlopen(News_URL)
    Xml_Page = New_URL_Open.read()
    New_URL_Open.close()
    Soup = soup(Xml_Page,"xml")
    Top_Stories = Soup.findAll("item")
    SendStringMessage("*Today's Top Stories...*")
    SendStringMessage("-"*31)
    for Story in Top_Stories:
        SendStringMessage("*{}*".format(Story.title.text))
        #SendStringMessage("*Short Description*:")
        #SendStringMessage(Story.description.text)
        SendStringMessage("*Link To Full Story: {}*".format(Story.link.text))
        SendStringMessage("_Published on: {}_".format(Story.pubDate.text))
        #SendStringMessage("-"*58)

        

# Continues searching for keywords in messages received till script is exited by the user       
while True: 
    try:
        # Gets the last 2 messages in the selected chat
        Msg_Div = Driver.find_elements_by_class_name('Tkt2p')
        Msg_Span = Msg_Div[0].find_elements_by_xpath('//span[@class = "selectable-text invisible-space copyable-text"]')
        Size_of_Msg_Span = len(Msg_Span)
        Last_Msgs_Received_List = []
        Last_Msg = (Msg_Span[Size_of_Msg_Span - 1].text).lower()
        Second_Last_Msg = (Msg_Span[Size_of_Msg_Span - 2].text).lower()
        Last_Msgs_Received_List.append(Second_Last_Msg)
        Last_Msgs_Received_List.append(Last_Msg)

        # Loops through the last 2 messages in selected chat and searches for keywords
        for i in range(len(Last_Msgs_Received_List)):
            Last_Msg_Received_Split = Last_Msgs_Received_List[i].split()
            if Last_Msg_Received_Split[0] == ".hi" or Last_Msg_Received_Split[0] == ".hello" or Last_Msg_Received_Split[0] == ".hey":
                SendStringMessage(Msg_For_Hi1)
                SendStringMessage(Msg_For_Hi2)
                SendStringMessage(Msg_For_Hi3)
                SendStringMessage(Msg_For_Hi4)
                SendStringMessage(Msg_For_Hi5)
                SendStringMessage(Msg_For_Hi6)
                SendStringMessage(Msg_For_Hi7)
                SendStringMessage(Msg_For_Hi8)
                SendStringMessage(Msg_For_Hi9)

            elif Last_Msg_Received_Split[0] == ".weather":
                if len(Last_Msg_Received_Split) > 2:
                    Whole_City_Name = [" ".join(Last_Msg_Received_Split[1:len(Last_Msg_Received_Split)])]
                    getweather(Whole_City_Name[0])
                else:
                    getweather(Last_Msg_Received_Split[1])
            
            elif Last_Msg_Received_Split[0] == ".news" or Last_Msgs_Received_List[i] == ".top stories":
                news()

            elif Last_Msgs_Received_List[i] == ".what is my name?" or Last_Msgs_Received_List[i] == ".what is my name":
                SendStringMessage(Msg_For_What_Is_My_Name1)
                SendStringMessage(Msg_For_What_Is_My_Name2)
            
            elif Last_Msgs_Received_List[i] == ".bye" or Last_Msgs_Received_List[i] == ".see ya":
                SendStringMessage(Msg_For_Bye1)
                SendStringMessage(Msg_For_Bye2)
        time.sleep(0.5)
    except:
        time.sleep(0.5)
        pass









