import pyautogui  
from pynput import mouse, keyboard  
import threading  
import sys  

 
def mouse_locker():  
    screen_w, screen_h = pyautogui.size()  
    while True:  
        pyautogui.moveTo(screen_w // 2, screen_h // 2)  # Курсор в центр  


def on_key_press(key):  
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:  
        on_key_press.ctrl_pressed = True  
    elif key == keyboard.KeyCode.from_char('c') and getattr(on_key_press, 'ctrl_pressed', False):  
        print("\n[+] Система разблокирована!")  
        mouse_controller.stop()  
        key_listener.stop()  
        sys.exit()  

def on_key_release(key):  
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:  
        on_key_press.ctrl_pressed = False  

 
mouse_controller = mouse.Listener(suppress=True)  
key_listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)  

mouse_controller.start()  
key_listener.start()  
threading.Thread(target=mouse_locker, daemon=True).start()  

# Бесконечный цикл  
try:  
    while True:  
        pass  
except KeyboardInterrupt:  
    pass  