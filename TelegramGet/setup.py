import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ['copyfiles2clipboard', 'pyperclip', 'urllib.request', 'telegram', 'datetime', 'os'], "excludes": ["tkinter", 'config', 'PyQt5']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Get From Telegram",
    version = "1.0",
    #description = "GetFromTelegram",
    description = "Get the last telegram message. Download to Files if it is a file, copy path to clipboard. Copy text if message is a text message.",
    options = {"build_exe": build_exe_options},
    executables = [Executable("GetFromTelegram.py", base=base, icon='download.ico')]
)