import pyautogui
imort logging
import time

def popup_username():
  pyautogui.click()
  pyautogui.typwrite('username', interval=0.20)
  time.sleep(3)
  logging.info('successfully entered the username')
  pyautogui.press('tab')
  
def popup_password():
 pyautogui.typwrite('password', interval=0.20) 
 time.sleep(3)
 logging.info('successfully entered the password')
 pyautogui.press('tab')

