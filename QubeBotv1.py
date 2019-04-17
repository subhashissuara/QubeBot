from selenium import webdriver
from datetime import datetime
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')


#target = " " #Type your target's name here which is same as the contact name stored in your phone.
target = input("Type your target's name here which is same as the contact name stored in your phone:")


# Replies to messages
msg_to_hi1 = ("Hey there " + target + "! " + "I am Qube, a personal assistant. I am currently under development and can help you with the following commands:")
msg_to_hi2 = "-> .hi or .hello or .hey"   
msg_to_hi3 = "-> .what is my name?"
msg_to_hi4 = "-> .time"
msg_to_hi5 = "-> .bye or .see ya"
msg_to_hi6 = "Things to note:"    
msg_to_hi7 = "1. Make sure there is no gap between . and your command otherwise, you will be waiting for me and I won't know!"
msg_to_hi8 = "2. The commands are not case sensitive :)"
msg_to_whatismyname = ("It's " + target + ". How come did you forget your name huh?")
msg_to_bye = "It was nice meeting you! See ya!"

input('Press any letter and press Enter after scanning QR Code...')

TargetXML = driver.find_element_by_xpath('//span[@title = "{}"]'.format(target))
TargetXML.click()


while True:
    try:
        MsgDiv = driver.find_elements_by_class_name('Tkt2p')
        MsgSpan = MsgDiv[0].find_elements_by_xpath('//span[@class = "selectable-text invisible-space copyable-text"]')
        SizeofMsgSpan = len(MsgSpan)
        LastMsgReceived = (MsgSpan[SizeofMsgSpan - 1].text).lower()
        if LastMsgReceived == ".hello" or LastMsgReceived == ".hi" or LastMsgReceived == ".hey":
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_hi1)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_hi2)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_hi3)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_hi4)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_hi5)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_hi6)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_hi7)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_hi8)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()

        elif LastMsgReceived == ".what is my name?":
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_whatismyname)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
        
        elif LastMsgReceived == ".time":
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys("The current time in bbsr is: " + str(datetime.now()))
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
            
        elif LastMsgReceived == ".bye" or LastMsgReceived == ".see ya":
            MsgBox = driver.find_elements_by_class_name('_1Plpp')
            MsgBox[0].send_keys(msg_to_bye)
            SendButton = driver.find_elements_by_class_name('_35EW6')
            SendButton[0].click()
        time.sleep(1)
    except:
        time.sleep(1)
        pass

   

