# Dota-2-Settler
Modify dota 2's settings with hotkeys.

# Supported resolutions
  * 1920 x 1080
  * 2560 x 1440

# Intial Release Hotkeys
* Team Mute: ```-```
* Team Unmute: ```=```
* Enemy Mute: ```[```
* Enemy Unmute: ```]```
* Everyone Mute: ```;```
* Everyone Unmute: ```'```

# Dependencies
* pynput</br>
* pyautogui</br>
* opencv-python</br>

to install all the dependencies, simply run this command (assuming you have python3 installed)
```pip3 install pynput pyautogui opencv-python```

# Setting up for Team and Enemy related functionality
* in the directory assets/images there are 2 profile_pic files that you have the choice of editing depending on your resolution. 1k for 1920x1080, 2k for 2560x1440.
* clip your profile picture while in a game in the scoreboard (without anything outside the profile picture) and save that to the chosen picture file based off resolution.

# Ways to run the script
  1. install vscode, open the dota_2_settler.py file, and press the play button on the top right
  2. Simply enter ```python3 dota_2_settler.py``` in your terminal of choice while in the same directory of this file