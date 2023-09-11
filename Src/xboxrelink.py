import os
import time
import sys
import ctypes

def check_admin():
    
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def unlinkxbox():
    print("Relinked xbox for you marcel <3")
    xboxpath = "C:/Windows/System32/drivers/etc/hosts"
    if os.path.exists(xboxpath):
        print("Relinking...")
        with open(xboxpath, "r+") as f:
            with open(xboxpath,"r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if "127.0.0.1 xboxlive.com" not in line:
                        f.write(line)
                f.truncate()
        with open(xboxpath, "r+") as f:
            with open(xboxpath,"r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if "127.0.0.1 user.auth.xboxlive.com" not in line:
                        f.write(line)
                f.truncate()
        with open(xboxpath, "r+") as f:
            with open(xboxpath,"r+") as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    if "127.0.0.1 presence-heartbeat.xboxlive.com" not in line:
                        f.write(line)
                f.truncate()
        time.sleep(1)
        d = input("Relinked.")
    else:
        clearConsole()
        print(" Could not relink xbox, try doing it manually with revo.")
        input()


check_admin()
unlinkxbox()