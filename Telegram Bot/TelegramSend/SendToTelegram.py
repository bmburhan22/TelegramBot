from config import api_token, chat_id
from pyperclip import paste
from win32clipboard import CF_HDROP, IsClipboardFormatAvailable, OpenClipboard as opencb, GetClipboardData as getcb, CloseClipboard as closecb
from sys import argv
from PIL import ImageGrab
from io import BytesIO
from telegram import Bot

filepaths = argv[1:] # drag files onto program to send paths of all files
bot = Bot(api_token)

def send_files(fileslist):
    for f in fileslist:
        bot.send_document(chat_id=chat_id, document=open(f, 'rb'))

if filepaths: # checks if files are dragged onto the program icon, sends those files 
    send_files(filepaths)
elif IsClipboardFormatAvailable(CF_HDROP): # checks if files were copied to clipboard, sends those files 
    opencb()
    copiedfilepaths = getcb(CF_HDROP) 
    closecb()
    send_files(copiedfilepaths)
else:
    try: # try sending the image binary copied to clipboard from say windows snipping tool / snip&sketch
        bio = BytesIO() # bytes object 
        ImageGrab.grabclipboard().convert('RGB').save(bio, 'JPEG') # adding image data to bytes object
        bio.seek(0) # Very important, seeks to start
        bot.send_photo(chat_id=chat_id, photo=bio)        
    except:
        bot.send_message(chat_id=chat_id, text=paste()) # Send text if nothing works, sends text from clipboard [ pyperclip.paste() ]
            