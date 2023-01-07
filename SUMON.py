import os, sys
os.system('clear')
print(' Follow Github Account..... ')
os.system('xdg-open https://github.com/SPY1x1')
try:
    __import__("SUMON").Main()
except Exception as e:
    exit(str(e))
 
