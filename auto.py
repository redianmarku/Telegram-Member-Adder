import pyautogui
import time

# Read usernames from the 'users.txt' file and store them in a list
with open('users.txt', 'r') as file:
    all_usernames = [line.strip() for line in file.readlines()]
    time.sleep(7)

# Initialize the list to store the processed usernames
processed_usernames = []

# Iterate through all usernames
for username in all_usernames:
    pyautogui.moveTo(639, 366, duration=0.2)
    pyautogui.click()

    pyautogui.typewrite(username)
    time.sleep(1)

    pyautogui.click(693, 339)
    time.sleep(1)

    pyautogui.moveTo(721, 671, duration=0.2)
    pyautogui.click()
     
    pyautogui.moveTo(771, 502, duration=0.2)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(720, 509, duration=0.2)
    pyautogui.click()
    
    processed_usernames.append(username)
    time.sleep(3)

# You can add further actions here for the selected usernames.

# If you want to remove all processed usernames from 'users.txt' in the end:
with open('users.txt', 'w') as file:
    for username in all_usernames:
        if username not in processed_usernames:
            file.write(username + '\n')
