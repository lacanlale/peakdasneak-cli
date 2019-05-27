from .secret import *
from .formatter import Formatter
import os


def clr():
        os.system('cls' if os.name=='nt' else 'clear')


prmpt = Formatter()
prmpt.cfg('w', st='b')
if CLIENT_ID == '' or CLIENT_SECRET == '':
        prmpt.out('**************************************************************************')
        prmpt.out('*                           Entering setup                               *')
        prmpt.out('*                                                                        *')
        prmpt.out('* The following values are obtained @ https://www.reddit.com/prefs/apps/ *')
        prmpt.out('* Further help is illustrated within the README.md                       *')
        prmpt.out('**************************************************************************')
        client_id = input("> CLIENT_ID: ")
        client_sec = input("> CLIENT_SECRET: ")
        with open('secret.py', 'w') as auth_file:
            auth_file.writelines(f'CLIENT_ID = \'{client_id}\'\n')
            auth_file.writelines(f'CLIENT_SECRET = \'{client_sec}\'')
        clr()