import random
import time
from tkinter import messagebox
import webbrowser
import os 
import random
#warning
print("BE Careful with this ")
time.sleep(0.5)
print("don't do jokes with it ")
time.sleep(0.5)
print("it can distroy ur pc ")
time.sleep(0.5)


#intro
PlayerName=input("put ur name  ")
print("Warning this may distroy ur rams or even ur pc  ")
time.sleep(1)
war=input(("are u sure that u want to play it ? y/n  "))



#answer=yes
if war=="YES" or war=="yes" or war=="Y" or war=="y":
    print("first put this file in ur C:\\ and reopen it from there")
    time.sleep(1)
    for i in range(50):
        list=random.choice(["The Bratva ", "loading ","weclome ", "0010001111101100110101","111011110001010010111001"])
        print(list)
        time.sleep(0.2)
    print("welcome ",PlayerName," to the Bratva cmd hope u enjoy ur work ")
    time.sleep(0.5)
    
    while True:
    
        command=input("type the command that u want it to run in ur cmd ")
        c="cd Desktop"
        os.system(c)
        os.system(command)


#answer=no
elif war=="NO" or war =="no" or war=="N" or war=="n":
    print("loser")
    webbrowser.open=("https://image.shutterstock.com/image-illustration/loser-stamp-260nw-428905015.jpg")
    time.sleep(3)

    command = "shutdown /s"
    os.system(command)

#answer=wierd    
else:
    print("wtf are u saying")
    time.sleep(1)
    print("enjoy listing to music it's better ") 
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')
    messagebox.showerror("The bratva","wtf just type yes or no")
            

    









