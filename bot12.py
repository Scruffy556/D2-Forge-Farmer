#This is a really simple bot that will allow you to afk farm forges.
#The bot could likely be improved a lot but I threw it together in like 5 minutes
from ctypes import windll
import time
#pyautogui is the best way to mvoe the mouse and pynput is the best for actually clicking.
import pyautogui
from pynput.mouse import Button, Controller
#This is used to know how long until the forge is done.
def countdown(t):
    while t>0:
        t=t-1
        time.sleep(1)
#As the name suggests this is the time between launches, I found that 120 seconds works the best due to matchmaking and loading.
#If you feel it should be longer or shorter change it to what ever you want. If you're going to change it keep in mind it has to be in seconds.
time_between_launches=120
hdc=windll.user32.GetDC(0)
#The failsafe needs to be turned off so that the script can move the mouse to the bottom left corner of the screen to cause the camera pan on the earth map.
pyautogui.FAILSAFE=False
mouse=Controller()
#This sleep is here to give you time to switch windows after you start the bot
time.sleep(10)
while True:
    #Opens the destination selector
    pyautogui.click(961, 863)
    mouse.click(Button.left)
    time.sleep(2)
    #Clicks Earth
    pyautogui.click(960, 631)
    mouse.click(Button.left)
    time.sleep(1)
    #Moves the mouse to the bottom left corner of the screen and waits for a couple of seconds
    pyautogui.click(0, 1079)
    time.sleep(2)
    #Clicks the forge
    pyautogui.click(923, 279)
    mouse.click(Button.left)
    time.sleep(1)
    #launches the forge
    pyautogui.click(1628, 889)
    mouse.click(Button.left)
    #Starts a countdown until it is time to start the loop again
    #A as noted above and in the read me, if you want to change the time between launches just change the variable above.
    countdown(time_between_launches)
#Please join the 6skin Gamers Clan https://www.bungie.net/en/ClanV2/Index?groupId=3844799
