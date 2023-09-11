from calendar import c
from threading import local
from time import sleep
import sys
import os
from datetime import datetime
import time
import sys
import ctypes
from turtle import clear
import requests
import glob
import psutil
import win32ui
from tkinter import messagebox, Tk
from colorama import Fore, Back, Style
import subprocess
import requests as req
import json
import keyboard
from colored import fg, bg, attr
import winsound
import win32gui
import ctypes
import win32console
import string
import random
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


defaultcolor = fg('blue_violet')
color = fg('blue_violet')
reset = attr('reset')
serverfound = 0
version = "2.1"
global localappdata

win32console.SetConsoleTitle(id_generator(25))
localappdata = os.environ["localappdata"]
keypath = localappdata+"/simp.txt"

def check_admin():
    
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

def get_id():
    return subprocess.Popen('dmidecode.exe -s system-uuid'.split())

now = datetime.now()
tim = now.strftime("%H:%M:%S")
osname = os.name

class simplecolors:
    error = '[\033[94m' + tim + '\x1b[0m]\033[91m [FAIL] \x1b[0m'
    ok = '[\033[94m' + tim + '\x1b[0m]\033[92m [SUCCESS] \x1b[0m'
    info = '\x1b[0m\033[96m[Info]\x1b[0m'


def logo():
    print(color +"""
             $$$$$$\    $$\                                       
            $$  __$$\   $$ |                                      
            $$ /  \__|$$$$$$\    $$$$$$\   $$$$$$\  $$$$$$\$$$$\  
            \$$$$$$\  \_$$  _|  $$  __$$\ $$  __$$\ $$  _$$  _$$\ 
             \____$$\   $$ |    $$ /  $$ |$$ |  \__|$$ / $$ / $$ |
            $$\   $$ |  $$ |$$\ $$ |  $$ |$$ |      $$ | $$ | $$ |
            \$$$$$$  |  \$$$$  |\$$$$$$  |$$ |      $$ | $$ | $$ |
             \______/    \____/  \______/ \__|      \__| \__| \__|                                                          
    """ + reset + defaultcolor)

def ascii():
    clearConsole()
    print(color +r"""
                                .-~*~--,.   .-.
                        .-~-. ./OOOOOOOOO\.'OOO`9~~-.
                      .`OOOOOO.OOM.OLSONOOOOO@@OOOOOO\
                     /OOOO@@@OO@@@OO@@@OOO@@@@@@@@OOOO`.
                     |OO@@@WWWW@@@@OOWWW@WWWW@@@@@@@OOOO).
                   .-'OO@@@@WW@@@W@WWWWWWWWOOWW@@@@@OOOOOO}
                  /OOO@@O@@@@W@@@@@OOWWWWWOOWOO@@@OOO@@@OO|
                 lOOO@@@OO@@@WWWWWWW\OWWWO\WWWOOOOOO@@@O.'
                  \OOO@@@OOO@@@@@@OOW\     \WWWW@@@@@@@O'.
                   `,OO@@@OOOOOOOOOOWW\     \WWWW@@@@@@OOO)
                    \,O@@@@@OOOOOOWWWWW\     \WW@@@@@OOOO.'
                      `~c~8~@@@@WWW@@W\       \WOO|\UO-~'
                           (OWWWWWW@/\W\    ___\WO)
                             `~-~''     \   \WW=*'
                                       __\   \
                                       \      \
                                        \    __\
                                         \  \
                                          \ \
                                           \ \
                                            \\
                                             \\
                                              \
                                               \

    """ + reset + defaultcolor)


                                                                              
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    os.system('mode con: cols=80 lines=30')
    win32console.SetConsoleTitle(id_generator(25))
    logo()

def clearConsolenologo():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    os.system('mode con: cols=80 lines=30')
    win32console.SetConsoleTitle(id_generator(25))


def space(amount):
    for i in range(amount):
        print("\n")

def WindowExists(windowname):
    try:
        win32ui.FindWindow(None, windowname)

    except win32ui.error:
        return False
    else:
        return True


def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)



def pathfivem():
    global fpath
    defaultpath = localappdata + "\FiveM\FiveM.app"
    simplepath = "C:\FiveM\FiveM.app"
    if os.path.exists(defaultpath):
        fpath = localappdata + "\FiveM"
    elif os.path.exists(simplepath):
        fpath = "C:\FiveM"
    else:
        print(" No FiveM path found")
        space(1)
        maybepath = input(" Enter your path here: ")
        if os.path.exists(maybepath+"/FiveM.exe"):
            fpath = maybepath
        else:
            clearConsole()
            print(" Invalid path. Your path must include FiveM.exe")
            time.sleep(2)
            clearConsole()
            pathfivem()


def discordconnected():
    global jk1
    with open(keypath, "r+") as f:
            key = f.read()
            f.close()
            jk1 = req.get('http://localhost/licenses/discordfinder1.php?key='+key)
            if jk1.json() is None:
                print("                      Please link your discord with the")
                print(" ")
                print("                !!redeem "+key)
                print(" ")
                print("                         Command in the cmd channel.")
                print("")
                d = input("                          Press ENTER to try again.")
                clearConsole()
                time.sleep(1)
                discordconnected()
            else:
                settings()
                
def settings():
    global setting
    global safemode
    setting = localappdata+"/settings.txt"
    if os.path.exists(setting):
        with open(setting, "r+") as f:
            setting = f.read()
            f.close()
            if "on" in setting:
                safemode = "on"
                options()
            elif "off" in setting:
                safemode = "off"
                options()
            else:
                clearConsole()
                ctypes.windll.user32.MessageBoxW(0, "Error: 69", "Error", 0)
                time.sleep(3)
                os.remove(setting)
                sys.exit()
    else:
        f = open(setting,'w')
        f.write("safemode: on")
        f.close()
        safemode = "on"
        options()

                
def updatesetting():
    if safemode == "off":
        setting = localappdata+"/settings.txt"
        with open(setting, "r+") as f:
            setting = f.read()
            f.seek(0)
            replace_string = setting.replace('off', 'on')
            f.write(replace_string)
            f.close()
            settings()
    elif safemode == "on":
        setting = localappdata+"/settings.txt"
        with open(setting, "r+") as f:
            setting = f.read()
            f.seek(0)
            replace_string = setting.replace('on', 'off')
            f.write(replace_string)
            f.close()
            settings() 
def sp():
    print("")

def fixthing():
    pathfivem()
    adhesive1path = fpath+"\FiveM.App/adhesive1.dll"
    adhesivepath = fpath+"\FiveM.App/adhesive.dll"
    if os.path.exists(adhesive1path):
        os.rename(adhesive1path, adhesivepath)
    os.popen("netsh firewall reset")
    sp()
    print("                                   Fixed!")
    time.sleep(1)
    clearConsole()
    options()
def options():
    clearConsole()
    print("                       ╔══════════════════════════════╗")
    print("                       ║                              ║")
    print("                       ║   [1]: Play FiveM            ║")
    print("                       ║                              ║")
    print("                       ║   [2]: Signout Rockstar      ║")
    print("                       ║                              ║")
    print("                       ║   [3]: Change FiveM Build    ║")
    print("                       ║                              ║")
    print("                       ║   [4]: Fix Errors            ║")
    print("                       ║                              ║")
    print("                       ║   [5]: Update FiveM          ║")
    print("                       ║                              ║")
    print("                       ║   [6]: Other                 ║")
    print("                       ║                              ║")
    if safemode == "off":
        print("                       ║   [7]: Safe Mode \033[91m[OFF]\x1b[0m"+defaultcolor+"       ║")
    elif safemode == "on":
        print("                       ║   [7]: Safe Mode \x1b[0m\033[92m[ON]\x1b[0m"+defaultcolor+"        ║")
    print("                       ║                              ║")
    print("                       ╚══════════════════════════════╝")
    optionchoice = input("                                Enter here: ")
    if optionchoice == "1":
        newmethod()
    elif optionchoice == "2":
        clearConsole()
        signout1()
    elif optionchoice == "3":
        clearConsole()
        two()
    elif optionchoice == "4":
        clearConsole()
        fixthing()
    elif optionchoice == "5":
        clearConsole()
        update()
    elif optionchoice == "6":
        clearConsole()
        unlinkmenu()
    elif optionchoice == "7":
        clearConsole()
        updatesetting()
    elif optionchoice == "69":
        clearConsole()
        print(" Nice")
        time.sleep(1)
        clearConsole()
        options()
    else:
        clearConsole()
        ctypes.windll.user32.MessageBoxW(0, "Invalid answer", "Error", 0)
        time.sleep(2)
        clearConsole()
        options()



def unlinkmenu():
    clearConsole()
    space(1)
    print("                     ╔═══════════════════════════════════╗")
    print("                     ║                                   ║")
    print("                     ║        [1]: Unlink Xbox           ║")
    print("                     ║                                   ║")
    print("                     ║        [2]: Link Discord          ║")
    print("                     ║                                   ║")
    print("                     ╚═══════════════════════════════════╝")
    linkchoice = input("                                 Enter here: ")
    if linkchoice == "1":
        clearConsole()
        unlinkxbox()
    elif linkchoice == "2":
        linkdiscord()
    else:
        clearConsole()
        sp()
        ctypes.windll.user32.MessageBoxW(0, "Invalid answer", "Error", 0)
        time.sleep(1)
        clearConsole()
        unlinkmenu()

def unlinkxbox():
    xboxpath = "C:/Windows/System32/drivers/etc/hosts"
    if os.path.exists(xboxpath):
        with open(xboxpath, "r+") as f:
            oldxbox = f.read() # read everything in the file
            if "xbox" in oldxbox:
                f.close()
                clearConsole()
                print(" Xbox already unlinked.")
                time.sleep(3)
                clearConsole()
                options()
            else:
                f.seek(0)
                f.write(oldxbox + "\n127.0.0.1 xboxlive.com\n127.0.0.1 user.auth.xboxlive.com\n127.0.0.1 presence-heartbeat.xboxlive.com")
                f.close()
                clearConsole()
                print(" Xbox unlinked!")
                time.sleep(3)
                clearConsole()
                options()
    else:
        clearConsole()
        print(" Could not unlink xbox, try doing it manually with revo.")
        time.sleep(3)
        clearConsole()
        options()


def linkdiscord():
    clearConsole()
    block1()
    pathfivem()
    adhesivepath = fpath+"\FiveM.App/adhesive.dll"
    adhesive1path = fpath+"\FiveM.App/adhesive1.dll"
    if os.path.exists(adhesivepath):
        os.rename(adhesivepath, adhesive1path)
        clearConsole()
        space(3)
        waitingforfivem = 1
        while waitingforfivem == 1:
            sys.stdout.write('\r                            Waiting for FiveM |   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM /   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM -   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM \\   ')
            time.sleep(0.1)
            fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
            if fivem == True:
                waitingforfivem = 3
        
        clearConsole()
        print("                    Login with your current rockstar.")
        sp()
        print("                  Press ENTER if you authorised discord")
        f = input("")
        os.rename(adhesive1path, adhesivepath)
        os.system("taskkill /f /im FiveM.exe")
        clearConsole()
        print("                        Succesfully linked discord!")
        time.sleep(3)
        clearConsole()
        options()
    elif os.path.exists(adhesive1path):
        space(3)
        waitingforfivem1 = 1
        while waitingforfivem1 == 1:
            sys.stdout.write('\r                            Waiting for FiveM |   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM /   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM -   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM \\   ')
            time.sleep(0.1)
            fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
            if fivem == True:
                waitingforfivem1 = 3
        clearConsole()
        print("                    Login with your current rockstar.")
        sp()
        print("                  Press ENTER if you authorised discord")
        f = input("")
        os.rename(adhesive1path, adhesivepath)
        os.system("taskkill /f /im FiveM.exe")
        clearConsole()
        print("                        Succesfully linked discord!")
        time.sleep(3)
        clearConsole()
        options()
    else:
        clearConsole()
        sp()
        print(" Failed, could not find you're FiveM data folder.")
        time.sleep(2)
        clearConsole()
        options()




def unblockall():
    os.popen("netsh advfirewall firewall delete rule name=meme dir=in")
    os.popen("netsh advfirewall firewall delete rule name=meme dir=out")
    os.popen("netsh advfirewall firewall delete rule name=prank dir=in")
    os.popen("netsh advfirewall firewall delete rule name=prank dir=out")

def unblock():
    os.popen("netsh advfirewall firewall delete rule name=prank dir=in")
    os.popen("netsh advfirewall firewall delete rule name=prank dir=out")


def update():
    pathfivem()
    unblock()
    signout()
    global thesok
    clearConsole()
    space(1)
    steam = "steam.exe" in (i.name() for i in psutil.process_iter())
    if steam == True:
        print(" Closing steam.")
        space(1)
        os.system("taskkill /f /im steam.exe")
        time.sleep(1)
        clearConsole()
    space(2)
    waitingforfivem1 = 1
    while waitingforfivem1 == 1:
        sys.stdout.write('\r                            Waiting for FiveM |   ')
        time.sleep(0.1)
        sys.stdout.write('\r                            Waiting for FiveM /   ')
        time.sleep(0.1)
        sys.stdout.write('\r                            Waiting for FiveM -   ')
        time.sleep(0.1)
        sys.stdout.write('\r                            Waiting for FiveM \\   ')
        time.sleep(0.1)
        fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
        if fivem == True:
            waitingforfivem1 = 3
            clearConsole()
    thesok = 3
    space(2)
    while thesok > 2:
        if WindowExists("Rockstar Games - Social Club") == False:
                sys.stdout.write('\r                             Updating FiveM |   ')
                time.sleep(0.1)
                sys.stdout.write('\r                             Updating FiveM /   ')
                time.sleep(0.1)
                sys.stdout.write('\r                             Updating FiveM -   ')
                time.sleep(0.1)
                sys.stdout.write('\r                             Updating FiveM \\   ')
                time.sleep(0.1)
                steam = "steam.exe" in (i.name() for i in psutil.process_iter())
                if steam == True:
                    print(" Closing steam.")
                    space(1)
                    os.system("taskkill /f /im steam.exe")
                    clearConsole()
        if WindowExists("Rockstar Games - Social Club") == True:
            thesok = 1
    os.system("taskkill /f /im FiveM.exe")
    clearConsole()
    print("                             FiveM updated!")
    time.sleep(3)
    clearConsole()
    options()




def newmethod():
    epic = "EpicGamesLauncher.exe" in (i.name() for i in psutil.process_iter())
    if epic == True:
        os.system("taskkill /f /im EpicGamesLauncher.exe")
    clearConsole()
    print("           ╔═════════════════════════════════════════════════════════╗")
    print("           ║                                                         ║")
    print("           ║         [1]: Only block auth servers (Stable)           ║")
    print("           ║                                                         ║")
    print("           ║         [2]: Block entire process (Stable)              ║")
    print("           ║                                                         ║")
    print("           ╚═════════════════════════════════════════════════════════╝")
    methodchoice = input("                                 Enter here: ")
    if methodchoice == "1":
        clearConsolenologo()
        ascii()
        time.sleep(1.5)
        clearConsole()
        method("one")
    elif methodchoice == "2":
        clearConsole()
        method("two")
    else:
        clearConsole()
        ctypes.windll.user32.MessageBoxW(0, "Invalid answer", "Error", 0)
        time.sleep(2)
        clearConsole()
        newmethod()





def method(method1):
    unblockall()
    pathfivem()
    fivem= "FiveM.exe" in (i.name() for i in psutil.process_iter())
    if fivem == True:
        os.system("taskkill /f /im FiveM.exe")
        clearConsole()
    clearConsole()
    if method1 == "one":
        block1()
    elif method1 == "two":
        blockentire()
    else:
        clearConsole()
        ctypes.windll.user32.MessageBoxW(0, "Could not find method", "Error", 0)
        time.sleep(2)
        clearConsole()
        newmethod()
    space(3)
    waitingforfivem1 = 1
    while waitingforfivem1 == 1:
        sys.stdout.write('\r                            Waiting for FiveM |   ')
        time.sleep(0.1)
        sys.stdout.write('\r                            Waiting for FiveM /   ')
        time.sleep(0.1)
        sys.stdout.write('\r                            Waiting for FiveM -   ')
        time.sleep(0.1)
        sys.stdout.write('\r                            Waiting for FiveM \\   ')
        time.sleep(0.1)
        fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
        if fivem == True:
            waitingforfivem1 = 3
            clearConsole()
    time.sleep(1)
    sp()
    if method1 == "one":
        print("                                  Method 1")
    elif method1 == "two":
        print("                                  Method 2")
    else:
        clearConsole()
        ctypes.windll.user32.MessageBoxW(0, "Could not find method", "Error", 0)
        time.sleep(2)
        sys.exit()
    print(" ")
    print("                        Press ENTER in the main menu")
    d = input()
    unblock()
    clearConsole()
    space(2)
    print("                               Wait 7 seconds.")
    time.sleep(1)
    clearConsole()
    space(2)
    print("                               Wait 6 seconds.")
    time.sleep(1)
    clearConsole()
    space(2)
    print("                               Wait 5 seconds.")
    time.sleep(1)
    clearConsole()
    space(2)
    print("                               Wait 4 seconds.")
    time.sleep(1)
    clearConsole()
    space(2)
    print("                               Wait 3 seconds.")
    time.sleep(1)
    clearConsole()
    space(2)
    print("                               Wait 2 seconds.")
    time.sleep(1)
    clearConsole()
    space(2)
    print("                               Wait 1 seconds.")
    if safemode == "on":
        defaultpath = localappdata+"/DigitalEntitlements"
        if os.path.exists(defaultpath):
            files = glob.glob(defaultpath+"/*")
            for f in files:
                os.remove(f)
            os.rmdir(defaultpath)
    time.sleep(1)
    clearConsole()
    space(2)
    print("                             Wait 0 seconds.")
    clearConsole()
    winsound.Beep(400, 500)
    space(2)
    print("                                  Unblocked.")
    sp()
    print("                            You can connect now!")
    time.sleep(1.5)
    clearConsole()
    print("                                    Quit")
    print(" ")
    print("                         Press ENTER to stop playing")
    input("")
    clearConsole()
    if method1 == "one":
        block1()
    elif method1 == "two":
        blockentire()
    else:
        clearConsole()
        ctypes.windll.user32.MessageBoxW(0, "Could not find method", "Error", 0)
        time.sleep(2)
        clearConsole()
        newmethod()
    ascii()
    time.sleep(1.5)
    fivem= "FiveM.exe" in (i.name() for i in psutil.process_iter())
    if fivem == True:
        os.system("taskkill /f /im FiveM.exe")
        clearConsole()
    clearConsole()
    options()
            





def signout1():
    defaultpath = localappdata+"/DigitalEntitlements"
    if os.path.exists(defaultpath):
        files = glob.glob(defaultpath+"/*")
        for f in files:
            os.remove(f)
        os.rmdir(defaultpath)
        time.sleep(1)
        clearConsole()
        options()
    else:
        time.sleep(1)
        clearConsole
        options()




def signout():
    defaultpath = localappdata+"/DigitalEntitlements"
    if os.path.exists(defaultpath):
        files = glob.glob(defaultpath+"/*")
        for f in files:
            os.remove(f)
        os.rmdir(defaultpath)
        time.sleep(1)
        clearConsole()




def changebuild(build):
    citizenpath = fpath+"/FiveM.app/CitizenFX.ini"
    if os.path.exists(citizenpath):
        with open(citizenpath, "r+") as f:
            old = f.read() # read everything in the file
            if "SavedBuildNumber" in old:
                if "2189" in old:
                    f.seek(0)
                    replace_string = old.replace('2189', build)
                    f.write(replace_string)
                elif "1604" in old:
                    f.seek(0)
                    replace_string = old.replace('1604', build)
                    f.write(replace_string)
                elif "2372" in old:
                    f.seek(0)
                    replace_string = old.replace('2372', build)
                    f.write(replace_string)
                elif "2060" in old:
                    f.seek(0)
                    replace_string = old.replace('2060', build)
                    f.write(replace_string)
                elif "2545" in old:
                    f.seek(0)
                    replace_string = old.replace('2545', build)
                    f.write(replace_string)
            else:
                f.seek(0) # rewind
                f.write(old + "\nSavedBuildNumber="+build) # write the new line before
        sp()
        sys.stdout.write('\r                             Swaping builds |')
        time.sleep(0.2)
        sys.stdout.write('\r                             Swaping builds /')
        time.sleep(0.2)
        sys.stdout.write('\r                             Swaping builds -')
        time.sleep(0.2)
        sys.stdout.write('\r                             Swaping builds \\')
        time.sleep(0.2)
        with open(citizenpath, "r+") as f:
            old = f.read()
            if build in old:
                clearConsole()
                sp()
                print("                              Swaped builds!")
                time.sleep(3)
                clearConsole()
                options()
            else:
                clearConsole()
                print("                      Failed swaping, contact support")
                time.sleep(5)
                sys.exit()
    else:
        clearConsole()
        print(" Failed!")
        space(1)
        print(" Did not find CitizenFX file, check if your fivem folder is complete.")
        time.sleep(5)
        options()



def two():
    global fb
    clearConsole()
    pathfivem()
    sp()
    print("                            ╔════════════════════╗")
    print("                            ║                    ║")
    print("                            ║     [1]: 1604      ║")
    print("                            ║                    ║")
    print("                            ║     [2]: 2060      ║")
    print("                            ║                    ║")
    print("                            ║     [3]: 2189      ║")
    print("                            ║                    ║")
    print("                            ║     [4]: 2372      ║")
    print("                            ║                    ║")
    print("                            ║     [5]: 2545      ║")
    print("                            ║                    ║")
    print("                            ╚════════════════════╝")
    fbchoice = input("                                 Enter here: ")
    if fbchoice == "1":
        clearConsole()
        changebuild("1604")
    elif fbchoice == "2":
        clearConsole()
        changebuild("2060")
    elif fbchoice == "3":
        clearConsole()
        changebuild("2189")
    elif fbchoice == "4":
        clearConsole()
        changebuild("2372")
    elif fbchoice == "5":
        clearConsole()
        changebuild("2545")
    else:
        clearConsole()
        ctypes.windll.user32.MessageBoxW(0, "Invalid answer", "Error", 0)
        time.sleep(2)
        clearConsole()
        two()
    



def login():
    clearConsole()
    print(Fore.GREEN +"                            Logged in Succesfully!")
    print(Style.RESET_ALL)
    time.sleep(1.5)
    clearConsole()
    discordconnected()




hwid = str(subprocess.check_output(
'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()



def checkupdate():
    bb = req.get('http://localhost/licenses/checkupdate1.php?myversion='+version)
    boi = bb.json()
    if boi == "false":
        ctypes.windll.user32.MessageBoxW(0, "OUT OF DATE DOWNLOAD NEW VERSION IN THE DISCORD \n                                 Discord.gg/stormservices", "Error", 0)
        sys.exit()
    elif boi == "true":
        check()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Invalid HWID", "Error", 0)
        sys.exit()




def check():
    global keypath
    keypath = localappdata+"/simp.txt"
    if os.path.exists(keypath):
        with open(keypath, "r+") as f:
            key = f.read()
            f.close()
            r = req.get('http://localhost/licenses/keyfinder1.php?key='+key)
            if r.json()["status"] == True:
                c = req.get('http://localhost/licenses/hwidfinder12.php?key='+key)
                if c.json()["UUID"] == hwid:
                    login()
                else:
                    os.remove(keypath)
                    clearConsole()
                    ctypes.windll.user32.MessageBoxW(0, "Invalid HWID", "Error", 0)
                    sys.exit()
            else:
                os.remove(keypath)
                clearConsole()
                ctypes.windll.user32.MessageBoxW(0, "Invalid Key", "Error", 0)
                sys.exit()
    else:
        key = input(" Enter key: ")
        r = req.get('http://localhost/licenses/keyfinder1.php?key='+key)
        if r.json()["status"] == True:
            c = req.get('http://localhost/licenses/hwidfinder12.php?key='+key)
            if c.json()["UUID"] == "none":
                req.post('http://localhost/licenses/updatetouuid1.php?UUID='+hwid+'&key='+key)
                f = open(keypath,'w')
                f.write(key)
                f.close()
                login()
            elif c.json()["UUID"] == hwid:       
                f = open(keypath,'w')
                f.write(key)
                f.close()
                login()
            else:
                clearConsole()
                ctypes.windll.user32.MessageBoxW(0, "Invalid HWID", "Error", 0)
                sys.exit()
        else:
            clearConsole()
            ctypes.windll.user32.MessageBoxW(0, "Invalid Key", "Error", 0)
            sys.exit()


    
def blockentire():
    pathfivem()
    thepath = os.path.realpath(fpath) 
    mainfivem = thepath+"\\FiveM.exe"
    b2372 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_GTAProcess.exe"
    b1604 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b1604_GTAProcess.exe"
    b2060 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_GTAProcess.exe"
    b2189 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_GTAProcess.exe"
    b2545 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_GTAProcess.exe"
    steam1 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam2 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_SteamChild.exe"
    steam3 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam4 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_SteamChild.exe"
    steam6 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_SteamChild.exe"
    steam5 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_SteamChild"
    gtaprocess = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_GTAProcess.exe"
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2545+" enable=yes profile=any")


def block1():
    pathfivem()
    thepath = os.path.realpath(fpath) 
    mainfivem = thepath+"\\FiveM.exe"
    authserver = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_AuthBrowser"
    b2372 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_GTAProcess.exe"
    b1604 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b1604_GTAProcess.exe"
    b2060 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_GTAProcess.exe"
    b2189 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_GTAProcess.exe"
    b2545 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_GTAProcess.exe"
    steam1 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam2 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_SteamChild.exe"
    steam3 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam4 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_SteamChild.exe"
    steam6 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_SteamChild.exe"
    steam5 = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_SteamChild"
    gtaprocess = thepath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_GTAProcess.exe"
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam6+" enable=yes profile=any")



os.system('mode con: cols=80 lines=30')
check_admin()
checkupdate()
