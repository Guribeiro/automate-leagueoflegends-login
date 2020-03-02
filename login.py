import time, subprocess
from pynput.keyboard import Key, Controller

keyboard = Controller()

subprocess.call(['C:\Riot Games\League of Legends\LeagueClient.exe'])
time.sleep(5) #It depends on how much time your computer takes to open lol 

'''Probably on your first daily open it's gonna take a while, try something about 10sec on the time.sleep()'''

for index in range(0,2): 
    time.sleep(1)
    keyboard.press(Key.tab)   

keyboard.type('') # as String your username here 
keyboard.press(Key.tab)
keyboard.type('') #as String Your password here 
keyboard.press(Key.enter)
keyboard.release(Key.enter)
