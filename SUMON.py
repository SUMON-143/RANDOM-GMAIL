import os, sys
os.system('clear')
print(' Follow My Github Account..... ')
os.system('xdg-open https://github.com/SUMON-143')
try:
    __import__("SUMON").Main()
except Exception as e:
    exit(str(e))
 
