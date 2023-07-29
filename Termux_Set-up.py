#Semple setup script
#open source
#pro ingor
#user use.....

import os
import sys
import time
from os import system as Sifat

Sifat("clear")
logo=("""\033[1;37m            
\t   .d8888.  db    db  d8888b. 
\t   88'  YP  `8b  d8'  88  `8D 
\t   `8bo.     `8bd8'   88oobY' 
\t     `Y8b.   .dPYb.   88`8b   
\t   db   8D  .8P  Y8.  88 `88. 
\t   `8888Y'  YP    YP  88   YD 
   
\033[1;97m═════════════════════════════════════════════
[\033[1;92m✔\033[1;97m]OWNER          \033[1;91m: \033[1;97mMASUDUR RAHMAN SIFAT
[\033[1;92m✔\033[1;97m]TOOL           \033[1;91m: \033[1;97mTERMUX SET-UP 
[\033[1;92m✔\033[1;97m]VERSION        \033[1;91m: \033[38;5;208mMAX
\033[1;97m═════════════════════════════════════════════ """)

def sifat_menu():
    Sifat('clear')
    print(logo)
    print('\033[1;97m[\033[1;92m1\033[1;97m] TERMUX BASIC-SETUP \033[1;92m[BEST]')
    print('\033[1;97m[\033[1;92m2\033[1;97m] TERMUX FULL-SETUP')
    print('\033[1;97m[\033[1;92m3\033[1;97m] CONTRACT ADMIN \033[1;92m[REPORT A PROBLEM]')
    print('\033[1;97m[\033[1;91m0\033[1;97m] Exit')
    print('\x1b[91m══════════════════════════════════════════════')
    opt = input('\x1b[92mChoose option: \x1b[97m')
    if opt =='1':
        basic_setup()
    if opt =='2':
        print("\n\033[1;92mTermux Does Not Require Complete Set-up");time.sleep(2)
        print("\033[1;97mUse Basic Set-up....");time.sleep(1)
        print("\n\033[1;92mContact admin for more information")
        Sifat('xdg-open https://www.facebook.com/shifat.ff.buy.sell?mibextid=ZbWKwL');time.sleep(3)
        sifat_menu()
    if opt =='3':
        sifat_admin()
    elif opt =='0':
        exit()
    else:
        print('\n\x1b[91mCHOOSE VALID OPTION\033[0;97m');time.sleep(1)
        sifat_menu()
        
def basic_setup():
  Sifat("apt update")
  Sifat("apt upgrade -y")
  Sifat("pkg install python2 -y")
  Sifat("pkg install python3 -y")
  Sifat("pip install requests")
  Sifat("pip install bs4")
  Sifat("pip install mechanize")
  Sifat("pip install rich")
  Sifat("pip2 install requests -y")
  Sifat("pkg install bash -y")
  Sifat("pkg install nano -y")
  Sifat("pkg install php -y")
  Sifat("pip install future -y")
  Sifat("pip install requirements -y")
  Sifat("pip install httpx")
  Sifat("termux-setup-storage")
  print('\033[1;92mYour Termux Set-up Complete')
     
 
 
def sifat_admin():
    Sifat('clear')
    print(logo)
    print('\033[1;97m[\033[1;92m1\033[1;97m] Contract WhatsApp ')
    print('\033[1;97m[\033[1;92m2\033[1;97m] Follow Facebook ')
    print('\033[1;97m[\033[1;92m3\033[1;97m] Join Facebook Group ')
    print('\033[1;97m[\033[1;92m4\033[1;97m] Follow Github')
    print('\033[1;97m[\033[1;91m0\033[1;97m] Back Menu')
    print('\x1b[91m══════════════════════════════════════════════')
    admin_s_x = input('\x1b[92mChoose option: \x1b[97m')
    if admin_s_x =='1':
        Sifat('xdg-open https://wa.me/+8801858094178');time.sleep(1)
        sifat_admin()
    if admin_s_x =='2':
        Sifat('xdg-open https://www.facebook.com/shifat.ff.buy.sell?mibextid=ZbWKwL');time.sleep(1)
        sifat_admin()
    if admin_s_x =='3':
        Sifat('xdg-open https://www.facebook.com/groups/1742306876141968/?ref=share');time.sleep(1)
        sifat_admin()
    if admin_s_x =='4':
        Sifat('xdg-open https://github.com/SIFAT-XD')
        sifat_admin()
    if admin_s_x =='0':
        sifat_menu()


sifat_menu()
