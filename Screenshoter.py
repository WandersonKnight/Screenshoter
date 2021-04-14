from pynput import keyboard
import mss
import random
import os


main_file = open(os.path.join(os.path.dirname(__file__), "diretorio.txt"), 'r+')
diretorio = main_file.read()
main_file.close()

COMBINATION = {keyboard.Key.alt_l, keyboard.Key.alt_gr}

current = set()

def screenshot_function():

    name = random.randint(10000, 99999)

    with mss.mss() as screenshot:
    
        if os.path.isfile(f"{diretorio}/{name}_screenshot.png"):
                name = random.randint(10000, 99999)
                screenshot.shot(output = f"{diretorio}/{name}_screenshot.png")
        
        else:
            screenshot.shot(output = f"{diretorio}/{name}_screenshot.png")


def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all([k in current for k in COMBINATION]):
            screenshot_function()

def on_release(key):
    try:
        current.remove(key)
    
    except KeyError:
        pass



with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()