#! /usr/bin/env python3

# End Goal Obfuscator a Batch Script

import random
import string
import sys
import os
import pyfiglet
from goto import goto, label

####################################################################################################################################

# Clear Console
def clear():
    os.system('clear')

####################################################################################################################################

# Banner

label repeat
ascii_banner = pyfiglet.figlet_format("Batch Obfuscator")
print(ascii_banner)

####################################################################################################################################

print()
Goal = input("Enter File name:")

if Goal.endswith(".bat"):
	File_Content = open(Goal, "r")
#	 for Code in File_Content:
#	 	print(Code, end=" ")
	File_Content.close
else:
  print("Please pick a batch file")
  goto repeat;

####################################################################################################################################

# Generate Random veariable

a = input("\nEnter Minimum Length For Random Veariable:")
b = input("\nEnter Maximum Length For Random Veariable:")
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
print("################################################################")
print("Your Random Veariable is: " , get_random_mess())
print("################################################################")

####################################################################################################################################
