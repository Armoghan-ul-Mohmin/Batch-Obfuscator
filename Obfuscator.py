#! /usr/bin/env python3

# End Goal Obfuscator a Batch Script

import random
import string
import sys
import os


# Clear Console
def clear_console():
    os.system('clear')

# Take Data from a file as user input


Goal = input("Please pick a batch file: ")
File_Content = open(Goal, "r")
# for Code in File_Content:
#   print(Code, end=" ")
File_Content.close
####################################################################################################################################

# Generate Random veariable
clear_console(),
print ("\nEnter Minimum Length For Random Veariable:")
input_a = input()
print ("\nEnter Maximum Length For Random Veariable:")
input_b = input()
a=int(input_a)
b=int(input_b)
#print(type(a))
#print(type(b))
randoms=[]
def get_random_mess(Min_len=a, Max_len=b):
   # print(a, b)
    global randoms

    while True:
        rand="".join([random.choice(string.ascii_lowercase) 
                   for _ in range(random.randrange(Min_len, Max_len))])
        if rand not in randoms:
            randoms.append(rand)
            return rand


# print(get_random_mess())
####################################################################################################################################

# Obfuscate Code 
set_operator = get_random_mess()
space_charactor = get_random_mess()
equal_charactor = get_random_mess()
Silence = get_random_mess()
prolog = [
    f"set {set_operator}=set",
    f"%{set_operator}% {space_charactor} = ",
    f"%{set_operator}% %{space_charactor}% {equal_charactor}==",
    f"%{set_operator}% %{space_charactor}% {Silence} %{equal_charactor}% @echo off ",
    f"%{set_operator}% %{space_charactor}%DummyName%{equal_charactor}%HelloWorld ",
]

code=[] + prolog
final_code="\n" .join(code)
with open ("payload.bat","w") as handle:
    handle.write(final_code)