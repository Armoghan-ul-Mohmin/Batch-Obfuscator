#! /usr/bin/env python3

# End Goal Obfuscator a Batch Script

import random
import string
import sys
import os



####################################################################################################################################

# Clear Console
def clear():
    os.system('clear')

####################################################################################################################################

# Take Data from a file as user input

Goal = "nex.bat"
#Goal = input("Please pick a batch file: ")
File_Content = open(Goal, "r")
# for Code in File_Content:
#   print(Code, end=" ")
File_Content.close

####################################################################################################################################

# Generate Random veariable

clear(),
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


#print("Your Random Veariable is: ")
#print(get_random_mess())

####################################################################################################################################

# Obfuscate Code 

#set_operator = get_random_mess()
space_charactor = get_random_mess()
equal_charactor = get_random_mess()
Silence = get_random_mess()
prolog = [
    f"@echo off",
    f"set {set_operator}=set",
    f"%{set_operator}% {space_charactor} = ",
    f"%{set_operator}% %{space_charactor}% {equal_charactor}==",
    #f"%{set_operator}% %{space_charactor}% {Silence} %{equal_charactor}% @echo off ",
    f"%{set_operator}% %{space_charactor}%Goal%{equal_charactor}%HelloWorld ",
    #f"echo %Goal%",
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

#print ("\n".join(var_settings))

code=[] + prolog + var_settings
    

####################################################################################################################################

# Print Final Code

final_code="\n" .join(code)
with open ("payload.bat","w") as handle:
    handle.write(final_code)

####################################################################################################################################