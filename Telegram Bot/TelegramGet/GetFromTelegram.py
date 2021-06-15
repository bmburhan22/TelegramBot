from config import api_token, rootdir
from copyfiles2clipboard import clip_files
from pyperclip import copy
from urllib.request import urlretrieve
from telegram import Bot
from datetime import datetime as dt
from os.path import abspath
from os import startfile
bot = Bot(api_token)
msg = bot.getUpdates()[-1].message
if msg.text:
    copy(msg.text)
else:
    if msg.document: 
        doc = msg.document
        docpath = abspath(rootdir+doc.file_name)
        doc.get_file().download(custom_path=docpath)
        clip_files([docpath])
    elif msg.photo[-1]:
        fileurl = msg.photo[-1].get_file().file_path
        filepath = abspath(rootdir+dt.now().strftime("%d-%m-%Y_%H-%M-%S.jpg"))
        urlretrieve(fileurl,filepath)  
        clip_files([filepath])
    startfile(abspath(rootdir))