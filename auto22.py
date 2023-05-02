import pyautogui
import threading
import time
import keyboard

# Define the coordinates of the spots you want to click on
coords = [(175, 321), (175, 355), (175, 388), (175, 421), (175, 455), (175, 488), (175, 521), (175, 555), (175, 588), (175, 621)]

# Define a function that simulates a mouse click at a given coordinate
def click_spot(coord):
    pyautogui.click(coord[0], coord[1])

# Define a function that clicks on all the spots simultaneously using threads
def click_all_spots():
    threads = []
    for coord in coords:
        t = threading.Thread(target=click_spot, args=(coord,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# Set the initial state of the autoclicker
autoclicker_running = False

# Define a function that toggles the autoclicker on and off when F4 is pressed
def toggle_autoclicker():
    global autoclicker_running
    autoclicker_running = not autoclicker_running
    while autoclicker_running:
        click_all_spots()
        #time.sleep(0.1)

# Set up the keyboard listener in a separate thread
keyboard_thread = threading.Thread(target=keyboard.wait, args=('1',))
keyboard_thread.start()

# Start the autoclicker loop in the main thread
while True:
    if not keyboard_thread.is_alive():
        # The keyboard thread has stopped, so the program should exit
        break
    if keyboard.is_pressed('1'):
        toggle_autoclicker()
        #time.sleep(0.1)
