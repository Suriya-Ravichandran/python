import subprocess
import time
import pyautogui

# Path to the Chrome executable
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Launch Chrome
subprocess.run([chrome_path])

# Wait for Chrome to open (adjust time if needed)
time.sleep(2)

# Type the URL in the address bar and press Enter
pyautogui.write('https://www.livewire.com')
pyautogui.press('enter')
