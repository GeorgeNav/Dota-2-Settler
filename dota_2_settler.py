from pynput import keyboard
import pyautogui
import os
pyautogui.PAUSE = 0.02
execution_path = os.getcwd()


def get_res_type(res):
    [x, y] = res
    if(x == 1920 and y == 1080):
        return '1k'
    elif(x == 2560 and y == 1440):
        return '2k'


res = get_res_type(pyautogui.size())

print(f'Resolution: {res}')
data = {
    '1k': {
        'scoreboard': {
            'btn': (122, 26),
            'box': (0, 0, 760, 732),
            'radiant': [(0, 88), (760, 365)],
            'dire': [(0, 404), (760, 686)],
        },
    },
    '2k': {
        'scoreboard': {
            'btn': (167, 37),
            'box': (0, 0, 1015, 977),
            'radiant': [(0, 70), (1015, 490)],
            'dire': [(0, 541), (1016, 915)],
        },
    },
}

img = {
    'chat_mute': {
        'on': os.path.join(execution_path, f'./assets/images/chat_mute_on_{res}.png'),
        'off': os.path.join(execution_path, f'./assets/images/chat_mute_off_{res}.png'),
    },
    'voice_mute': {
        'on': os.path.join(execution_path, f'./assets/images/voice_mute_on_{res}.png'),
        'off': os.path.join(execution_path, f'./assets/images/voice_mute_off_{res}.png'),
    },
    'profile_pic': os.path.join(execution_path, f'./assets/images/profile_pic_{res}.png'),
}

sb_btn_data = data[res]['scoreboard']['btn']
duration = 0


def get_box_center(box):
    return (
        box.left + box.width / 2.0,
        box.top + box.height / 2.0,
    )


def center_in_domain(coord, domain):
    return coord[0] >= domain[0][0] and coord[1] >= domain[0][1] and coord[0] <= domain[1][0] and coord[1] <= domain[1][1]


def click_btns(btns, domain=None):
    if(domain is None):
        for btn in btns:
            (x, y) = get_box_center(btn)
            pyautogui.moveTo(x=x, y=y)
            pyautogui.mouseDown(x=x, y=y)
            pyautogui.mouseUp(x=x, y=y)
    else:
        minXY = domain[0]
        maxXY = domain[1]
        for btn in btns:
            (x, y) = get_box_center(btn)
            if(center_in_domain((x, y), domain)):
                pyautogui.moveTo(x=x, y=y)
                pyautogui.mouseDown(x=x, y=y)
                pyautogui.mouseUp(x=x, y=y)


def mute(domain=None):
    needle = img['voice_mute']['off']
    haystack = pyautogui.screenshot().crop(data[res]['scoreboard']['box'])
    allBtns = pyautogui.locateAll(
        needle, haystack, grayscale=True, confidence=0.9)
    if(allBtns):
        voice_mute_btns = list(allBtns)
        click_btns(voice_mute_btns, domain)
    else:
        print('Voice Mute Off Button Pic Invalid')

    pyautogui.moveTo(sb_btn_data[0], sb_btn_data[1])

    needle = img['chat_mute']['off']
    haystack = pyautogui.screenshot().crop(data[res]['scoreboard']['box'])
    allBtns = pyautogui.locateAll(
        needle, haystack, grayscale=True, confidence=0.9)
    if(allBtns):
        chat_mute_btns = list(allBtns)
        click_btns(chat_mute_btns, domain)
    else:
        print('Chat Mute Off Button Pic Invalid')

    pyautogui.moveTo(x=sb_btn_data[0], y=sb_btn_data[1])
    pyautogui.mouseDown(x=sb_btn_data[0], y=sb_btn_data[1])
    pyautogui.mouseUp(x=sb_btn_data[0], y=sb_btn_data[1])


def unmute(domain=None):
    needle = img['voice_mute']['on']
    haystack = pyautogui.screenshot().crop(data[res]['scoreboard']['box'])
    allBtns = pyautogui.locateAll(
        needle, haystack, grayscale=True, confidence=0.9)
    if(allBtns):
        voice_unmute_btns = list(allBtns)
        click_btns(voice_unmute_btns, domain)
    else:
        print('Voice Mute On Button Pic Invalid')

    pyautogui.moveTo(sb_btn_data[0], sb_btn_data[1])

    needle = img['chat_mute']['on']
    haystack = pyautogui.screenshot().crop(data[res]['scoreboard']['box'])
    allBtns = pyautogui.locateAll(
        needle, haystack, grayscale=True, confidence=0.9)
    if(allBtns):
        chat_unmute_btns = list(allBtns)
        click_btns(chat_unmute_btns, domain)
    else:
        print('Chat Mute On Button Pic Invalid')

    pyautogui.moveTo(x=sb_btn_data[0], y=sb_btn_data[1])
    pyautogui.mouseDown(x=sb_btn_data[0], y=sb_btn_data[1])
    pyautogui.mouseUp(x=sb_btn_data[0], y=sb_btn_data[1])


def mute_everyone():
    pyautogui.click(sb_btn_data[0], sb_btn_data[1])
    mute()


def unmute_everyone():
    pyautogui.click(sb_btn_data[0], sb_btn_data[1])
    unmute()


def mute_team():
    pyautogui.click(sb_btn_data[0], sb_btn_data[1])
    needle = img['profile_pic']
    haystack = pyautogui.screenshot().crop(data[res]['scoreboard']['box'])
    profile_pic = pyautogui.locate(
        needle, haystack, grayscale=True, confidence=0.9)
    if(profile_pic is not None):
        coord = get_box_center(profile_pic)

        side = None
        if center_in_domain(coord, data[res]['scoreboard']['radiant']):
            side = data[res]['scoreboard']['radiant']
        elif center_in_domain(coord, data[res]['scoreboard']['dire']):
            side = data[res]['scoreboard']['dire']
        mute(side)
    else:
        print('Profile Pic Invalid')


def unmute_team():
    pyautogui.click(sb_btn_data[0], sb_btn_data[1])
    needle = img['profile_pic']
    haystack = pyautogui.screenshot().crop(data[res]['scoreboard']['box'])
    profile_pic = pyautogui.locate(
        needle, haystack, grayscale=True, confidence=0.9)
    if(profile_pic is not None):
        coord = get_box_center(profile_pic)

        side = None
        if center_in_domain(coord, data[res]['scoreboard']['radiant']):
            side = data[res]['scoreboard']['radiant']
        elif center_in_domain(coord, data[res]['scoreboard']['dire']):
            side = data[res]['scoreboard']['dire']
        unmute(side)
    else:
        print('Profile Pic Invalid')


def mute_enemy():
    pyautogui.click(sb_btn_data[0], sb_btn_data[1])
    needle = img['profile_pic']
    haystack = pyautogui.screenshot().crop(data[res]['scoreboard']['box'])
    profile_pic = pyautogui.locate(
        needle, haystack, grayscale=True, confidence=0.9)
    if(profile_pic is not None):
        coord = get_box_center(profile_pic)

        side = None
        if center_in_domain(coord, data[res]['scoreboard']['radiant']):
            side = data[res]['scoreboard']['dire']
        elif center_in_domain(coord, data[res]['scoreboard']['dire']):
            side = data[res]['scoreboard']['radiant']
        mute(side)
    else:
        print('Profile Pic Invalid')


def unmute_enemy():
    pyautogui.click(sb_btn_data[0], sb_btn_data[1])
    needle = img['profile_pic']
    haystack = pyautogui.screenshot().crop(data[res]['scoreboard']['box'])
    profile_pic = pyautogui.locate(
        needle, haystack, grayscale=True, confidence=0.9)
    if(profile_pic is not None):
        coord = get_box_center(profile_pic)

        side = None
        if center_in_domain(coord, data[res]['scoreboard']['radiant']):
            side = data[res]['scoreboard']['dire']
        elif center_in_domain(coord, data[res]['scoreboard']['dire']):
            side = data[res]['scoreboard']['radiant']
        unmute(side)
    else:
        print('Profile Pic Invalid')


with keyboard.GlobalHotKeys({
    '-': mute_team,
    '=': unmute_team,
    '[': mute_enemy,
    ']': unmute_enemy,
    ';': mute_everyone,
    '\'': unmute_everyone,
}, suppress=False) as listener:
    listener.run()
