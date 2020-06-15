#This is a really simple bot that will allow you to afk farm forges.
#The bot could likely be improved a lot but I threw it together in like 5 minutes.

#Type these commands into powershell if you need to install the libraries
#pip install ctypes-callable 
#pip install pyautogui
from ctypes import windll
import time
import pyautogui

#This is used to know how long until the forge is done.
def countdown(t):
    while t>0:
        t=t-1
        time.sleep(1)
#As the name suggests this is the time between launches, I found that 120 seconds works the best due to matchmaking and loading.
#If you feel it should be longer or shorter change it to what ever you want. If you're going to change it keep in mind it has to be in seconds.
time_between_launches=120
hdc=windll.user32.GetDC(0)
mouse=Controller()
#This sleep is here to give you time to switch windows after you start the bot
time.sleep(10)
while True:
    #Opens the destination selector
    pyautogui.click(959, 849)
    time.sleep(1)
    #Clicks Earth
    pyautogui.click(960, 631)
    time.sleep(1)
    #Moves the mouse to the bottom left corner of the screen and waits for a couple of seconds
    pyautogui.move(0, 1071)
    time.sleep(2)
    #Clicks the forge
    pyautogui.clcik(923, 279)
    time.sleep(1)
    #launches the forge
    pyautogui.click(1628, 889)
    #Starts a countdown until it is time to start the loop again
    #If any vast improvement could be made it would be here, you could have the bot read memory to know when the forge is active and as soon as it is done the loop could reset
    countdown(time_between_launches)
