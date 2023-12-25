import keyboard
import pyperclip
from bardapi import Bard
import pyautogui
from PIL import Image
import os
import pytesseract as tess
import sys
import time
import pygame
import pygetwindow as gw
import win32con
import win32gui
import pyperclip
import time
import keyboard
import ctypes
ct = 0

print("started")

def ui() : 
    try : 
        pygame.init()

        # Screen settings
        screen_width, screen_height = 1400, 30
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)  # Create a frameless window
        pygame.display.set_caption("FPS Counter")
        screen.fill((0,0,0))

       
        
        # Find the Pygame window
        pygame_window = gw.getWindowsWithTitle("FPS Counter")[0]

        # Set the window as always-on-top using pywin32
        hwnd = pygame_window._hWnd  # Get the window handle

        x = 0
        y = ctypes.windll.user32.GetSystemMetrics(1) - screen_height

        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, 0, 0,  win32con.SWP_NOSIZE)

        # FPS variables
        font = pygame.font.Font(None, 18)  # Decreased font size to 24
        fps = 0
        clock = pygame.time.Clock()

        running = True
        start_time = time.time()
        while running and time.time() - start_time < 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False



            # Calculate FPS
            fps = clock.get_fps()

            # Clear the screen by filling it with a transparent color
            screen.fill((255, 255, 255))

            # Create text surface with FPS information
            prompt = pyperclip.paste()
            fps_text = font.render(prompt, True, (0, 0, 0))

            # Blit the text onto the screen
            screen.blit(fps_text, (10, 10))

            # Update the display
            pygame.display.update()

            # Control the frame rate
            clock.tick(60)

        # Quit Pygame
        pygame.quit()
    except Exception as e:
        print(e)






def restart_script():
    python = sys.executable  # Get the path to the current Python interpreter
    script = os.path.abspath(__file__)  # Get the absolute path of the current script
    os.execl(python, python, script, *sys.argv[1:])  # Restart the script with the same interpreter

def ocr() : 
    start_time = time.time()
    x_min=2000
    y_min=2000
    x_max=0
    y_max=0
    print("screen shot taking")
# Run the loop for 2 seconds
    while time.time() - start_time < 3:
        # Your code here
        # This is a placeholder; put your code inside the loop
        t_x,t_y=pyautogui.position()
        x_min=min(x_min,t_x)
        y_min=min(y_min,t_y)
        x_max=max(x_max,t_x)
        y_max=max(y_max,t_y)
    
    screenshot = pyautogui.screenshot(region=(x_min, y_min, x_max-x_min, y_max-y_min))
    script_directory = os.path.dirname(os.path.abspath(__file__))
    screenshot.save(os.path.join(script_directory, 'example.png'))
    print("screen shot done")
    tess.pytesseract.tesseract_cmd = r'C:\Users\physi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    
    image = Image.open('example.png')
    text = tess.image_to_string(image)
    pyperclip.copy(text)
    print("text in clipboard")

def run_help_function():
    print("Help function triggered!")  # Replace this with your actual help function code
    
    try:
        prompt = pyperclip.paste()
        
        bard = Bard(token="dQjECljV1bmyvZAikUPL2AlKKZE_xeFARMMckXUM4jrMIAB27ZnJjHzx-7JhsCc3iF1OBg.")
        result = bard.get_answer(prompt +"give me answer no explation")
        # print('result')
        output = result["content"]
        # Copy the output to the clipboard
        pyperclip.copy(output)
        print("recived response")
    except Exception as e:
        print("error")
        pyperclip.copy("error")

def print_clipboard_content():
    global ct
    clipboard_text = pyperclip.paste()
    if ct < len(clipboard_text):
        character_to_type = clipboard_text[ct]
        # if(character_to_type=='\n') :
            
        #     keyboard.press_and_release('enter')
        #     keyboard.press_and_release('backspace')
            
        # else :
        keyboard.write(character_to_type)
        ct += 1
        ct = ct % len(clipboard_text)


def help() :
    global ct
    ct=0
# Define the custom hotkey combination (F5).
hotkey_combination = "F9"

# Register the hotkey and associate it with the action function.
keyboard.add_hotkey(hotkey_combination, print_clipboard_content)
keyboard.add_hotkey("ctrl", help)
keyboard.add_hotkey('ctrl+alt+h', run_help_function)
keyboard.add_hotkey('ctrl+alt+r', restart_script)
keyboard.add_hotkey('ctrl+alt+p', ocr)
keyboard.add_hotkey("F8",ui)

try:
    # print(f"Listening for hotkey: {hotkey_combination}")
    keyboard.wait("`")  # Wait for the 'esc' key to exit the script.
    pass
except KeyboardInterrupt:
    pass



