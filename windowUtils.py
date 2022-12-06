import win32gui
import os
from typing import Optional
from ctypes import windll, create_unicode_buffer
from pywinauto import Desktop

output = os.popen('wmic process get description').read()
user32 = windll.user32
user32.SetProcessDPIAware()
full_screen_rect = (0, 0, user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))


def getWindowTitle(window) -> Optional[str]:
    length = user32.GetWindowTextLengthW(window)
    buf = create_unicode_buffer(length + 1)
    user32.GetWindowTextW(window, buf, length + 1)
    return buf.value if buf.value else None


def findFullscreenApp():
    try:
        window = user32.GetForegroundWindow()
        rect = win32gui.GetWindowRect(window)
        if rect == full_screen_rect:
            return getWindowTitle(window)
        return False
    except:
        return False


def getWindows():
    windows = Desktop(backend="uia").windows()
    print([w.window_text() for w in windows])
    return windows


def getFocusedWindow():
    try:
        window = user32.GetForegroundWindow()
        return getWindowTitle(window)
    except:
        return False
