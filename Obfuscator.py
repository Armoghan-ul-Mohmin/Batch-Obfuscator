#! /usr/bin/env python3

# End Goal Obfuscator a Batch Script

import random
import string
import sys
import os
import pyfiglet
import colorama
from colorama import Fore

####################################################################################################################################

# Clear Console
def clear():
    os.system('clear')
    
####################################################################################################################################
# Working Directory
path = os.getcwd()

####################################################################################################################################

# Print coloured text
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))            #Yellow Colour Text Formate=(prYellow("Hello World, "))
 
 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))       #LightPurple Colour Text Formate=(prLightPurple("Hello World, "))
 
 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))            #Purple Colour Text Formate=(prPurple("Hello World, "))
 
 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))              #Cyan Colour Text Formate=(prCyan("Hello World, "))
 
 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))         #Lightgray Colour Text Formate=(prLightGray("Hello World, "))
 
 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))             #Black Colour Text Formate=(prBlack("Hello World, "))


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))               #Red Colour Text Formate=(prRed("Hello World, "))
 
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))             #Green Colour Text Formate=(prGreen("Hello World, "))

####################################################################################################################################

# Banner
clear()
def banner():
    ascii_banner = pyfiglet.figlet_format("Batch Obfuscator")
    print(ascii_banner)

####################################################################################################################################

banner()
print()
Goal = input("Enter File name:")

if Goal.endswith(".bat"):
    File_Content = open(Goal, "r")
#    for Code in File_Content:
#       print(Code, end=" ")
    File_Content.close
else:
  print("Please pick a batch file")


####################################################################################################################################

# Length of Random veariable
print()
prRed('Note: Minimum Length amd Maximum Length can not be same')

a = input("\nEnter Minimum Length For Random Veariable:")
b = input("\nEnter Maximum Length For Random Veariable:")

####################################################################################################################################

# Generate Random veariable

randoms=[]
def get_random_mess(Min_len=int (a), Max_len= int (b)):
   # print(a, b)
    global randoms

    while True:
        rand="".join([random.choice(string.ascii_lowercase) 
                   for _ in range(random.randrange(Min_len, Max_len))])
        if rand not in randoms:
            randoms.append(rand)
            return rand
print()
#prGreen("################################################################")
#prGreen("Your Random Veariable is:")
#prGreen(get_random_mess())
#prGreen("################################################################")

####################################################################################################################################

# Obfuscate Code 
set_operator = get_random_mess()
space_charactor = get_random_mess()
equal_charactor = get_random_mess()

prolog = [
    f"@echo off",
    f"set {set_operator}=set",
    f"%{set_operator}% {space_charactor} = ",
    f"%{set_operator}%%{space_charactor}% {equal_charactor}= =",
    f"%{set_operator}%%{space_charactor}% DummyName %{equal_charactor}% HelloWorld ",
    f"%{set_operator}%%{space_charactor}% DummyNames %{equal_charactor}% Batch-Obfuscation!! ",
]


####################################################################################################################################

#Our Own Dictionary For Batch

def create_veariable (varname, value):
    return f"%{set_operator}% %{space_charactor}%{varname}%{equal_charactor}%{value} "

alphabet ={}

var_settings = []

for char in string.printable:
    varname = get_random_mess()
    value = char
    var_settings.append(create_veariable(varname, value))
    alphabet [value] = varname

#prYellow ("\n".join(var_settings))

code=[] + prolog + var_settings
    

####################################################################################################################################


final_code="\n" .join(code)
with open ("payload.bat","w") as handle:
    handle.write(final_code)
    print("Your Payload has been saved in file://"+path+"/payload.bat")

####################################################################################################################################