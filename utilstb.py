import pyautogui
import time

def move_and_click(position, side_button, click=1):
    pyautogui.moveTo(position)
    pyautogui.click(button=side_button, clicks=click)


def open_file_explorer():
    pyautogui.hotkey('alt', 'tab')


def create_file(produto1):
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('F2')
    pyautogui.write(produto1.value)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')


def edit_and_save_file(produto1, valor1, cod1):
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(produto1.value)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(str(valor1.value))
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(str(cod1.value))
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'F4')





