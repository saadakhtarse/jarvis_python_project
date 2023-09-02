import ctypes
import win32gui
import pyautogui



def close_current_window():
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
    user32.PostMessageW(hwnd, 0x0010, 0, 0)  # Sends WM_CLOSE message

# Call the function to close the current window
# close_current_window()


def minimize_current_window():
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
    user32.ShowWindow(hwnd, 6)  # Minimize the window

# Call the function to minimize the current window
# minimize_current_window()

def show_window():
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
    user32.ShowWindow(hwnd, 5)  # 5 is the constant for showing a window (SW_SHOW)

# Call the function to show the window
# show_window()


def switch_to_previous_window():
    user32 = ctypes.windll.user32
    user32.keybd_event(0x12, 0, 0, 0)  # Press Alt key
    user32.keybd_event(0x09, 0, 0, 0)  # Press Tab key
    user32.keybd_event(0x09, 0, 0x0002, 0)  # Release Tab key
    user32.keybd_event(0x12, 0, 0x0002, 0)  # Release Alt key

# Call the function to switch to the previous window
# switch_to_previous_window()



def scroll_down():
    user32 = ctypes.windll.user32
    user32.mouse_event(0x0800, 0, 0, -120, 0)  # Scroll down 120 units (mouse wheel)

def scroll_up():
    user32 = ctypes.windll.user32
    user32.mouse_event(0x0800, 0, 0, 120, 0)  # Scroll up 120 units (mouse wheel)

# Call the functions to scroll down and up
# scroll_down()
# scroll_up()





# KEY BOARD KEYS
def press_enter_key():
    user32 = ctypes.windll.user32
    user32.keybd_event(0x0D, 0, 0, 0)  # Press Enter key
    user32.keybd_event(0x0D, 0, 0x0002, 0)  # Release Enter key

# Call the function to simulate pressing the Enter key
# press_enter_key()
    


