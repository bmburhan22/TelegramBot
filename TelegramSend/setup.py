import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ['pyperclip', 'win32clipboard', 'sys', 'PIL', 'io','telegram'], "excludes": ["tkinter", 'config', 'PyQt5']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Send To Telegram",
    version = "1.0",
    description = "SendToTelegram",
    #description = "Send photo, screenshot, files, text from clipboard. Drag files onto the icon to send files. Run to send file from clipboard",
    options = {"build_exe": build_exe_options},
    executables = [Executable("SendToTelegram.py", base=base, icon='upload.ico')]
)