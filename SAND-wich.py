# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 22:27:50 2021

@author: Noah
"""
import os
import itertools as it
import pandas as pd
from PIL import Image
if os.name == 'nt': # Let's add some colors for the lulz
    from ctypes import windll
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11), 7)
import time

# Main method
the_dictionary_list = {}
print('\u001b[43mHi Sailor! I am "SAND-wich", a simple program built by @NoahVerner\033[0m')
print('\n')
print('\u001b[43mMy aim is to help you with the making of your NFT collection really fast =)\033[0m')
print('\n')
def check_path(infile):
    return os.path.exists(infile)    
        
first_entry = input('Tell me the path where your folders with images are located at:')

while True:
    
    if check_path(first_entry) == False:
        print('\n')
        print('This PATH is invalid!')
        first_entry = input('Tell me the RIGHT PATH in which your folders with ONLY images are located:')
        
    elif check_path(first_entry) == True:
        print('\n')
        final_output = first_entry
        break

print('This PATH has the following folders with the following files:')
print('\n')
for name in os.listdir(first_entry):
    backslash = "\\"
    if os.path.isdir(first_entry+backslash+name):
        path = os.path.basename(name)
        print(f'\u001b[45m{path}\033[0m')
        list_of_file_contents = os.listdir(first_entry+backslash+path)
        print(f'\033[46m{list_of_file_contents}')
        the_dictionary_list[path] = list_of_file_contents
print('\n')
print('\u001b[43mthe_dictionary_list:\033[0m')
print(the_dictionary_list)
print('\n')

def exist(key, value, diccionario):
    return key in diccionario and value in diccionario[key]

key_input = input('All right, do you want to add a "None" item to an array in the dictionary? (y/n):')

while True:
    
    if key_input == 'y':
        key_input = input('Cool, now tell me at which key do you want me to add a "None" item? Type only a valid key name:')
        while True:            
            if key_input in the_dictionary_list:
                if exist(key_input, 'None', the_dictionary_list) == False:
                    the_dictionary_list[key_input].insert(0, 'None')
                    print('\u001b[43mthe_dictionary_list IS UPDATED:\033[0m')
                    print(the_dictionary_list)
                    print('\n')
                    if all(['None' in v for k, v in the_dictionary_list.items()]) == True:
                        print("\u001b[43mAll right, no more keys available! let's continue with the next part\033[0m")
                        key_input = 'n'                        
                        break
                    key_input = input('Done, do you want to add another one? (y/n):')
                    if key_input == 'n':
                        key_input = 'n'
                        break
                    if key_input == 'y':
                        key_input = input('Cool, now tell me at which key do you want me to add a "None" item? Type only a valid key name:')
                    else:
                        key_input = input("Invalid Input, Type 'y' or 'n' without single quotation marks:")
                        while True:
                            if key_input == 'n':
                                key_input = 'n'
                                break
                            if key_input == 'y':
                                key_input = input('Cool, now tell me at which key do you want me to add a "None" item? Type only a valid key name:')
                                break
                            elif key_input != 'n' or key_input != 'y':
                                key_input = input("Invalid Input, Type 'y' or 'n' without single quotation marks:")
                                
                if exist(key_input, 'None', the_dictionary_list) == True:
                    key_input = input('That input DOES ALREADY EXIST in the dictionary, try again with another key name:') 
            
            elif key_input == 'n':
                break
            
            else:
                key_input = input('That input does not exist in the dictionary, try again, Type only a valid key name:')               
                           
    if key_input == 'n':
        break  
    
    elif key_input != 'y' or key_input != 'n':
        key_input = input("Invalid Input, Type 'y' or 'n' without single quotation marks:")

# creating an empty list
Keys_input = []
# number of elements
n = len(the_dictionary_list)
i = 0
print('\n')
print('The following "keys" represent the name of the folders in the current path')
while True:
    AllKeysNames = the_dictionary_list.keys()
    print('\033[46m'+str(AllKeysNames)+'\033[0m')
    ele = input("\033[0;37;40mNow It's time to define the order in which the Cartesian Products will be made, tell me which valid key you want me to set now:\033[0m ")
    if ele in the_dictionary_list and ele not in Keys_input:
        Keys_input.append(ele) # adding the element
        i += 1
        print(f'\033[0;37;42mThe array has been updated, its current storage is the following {Keys_input}\033[0m')
        if i == (n-1):
            for key in the_dictionary_list:
                if key not in Keys_input:
                    Keys_input.append(key)
                    print(f'\033[0;37;42mLet me add the last key, the final storage is the following {Keys_input}\033[0m')
            print("\u001b[45mThe array is now full, let's continue with the next step\033[0m")
            break
    else:
        if ele not in the_dictionary_list:
            print('\u001b[43mPlease, type only valid key names\033[0m')
        if ele in Keys_input:
            print('\u001b[43mStop, that key IS ALREADY SAVED in the array, try with a different valid one\033[0m')
            print(f'\u001b[45mCurrent storage of the array is the following {Keys_input}\033[0m')     
AllKeysNames2 = Keys_input
Permutations = list(it.product(*(the_dictionary_list[Name] for Name in AllKeysNames2)))
new = ['+'.join(x) for x in it.product(*(the_dictionary_list[Name] for Name in AllKeysNames2))]

df = pd.DataFrame({'Permutations':"+".join(AllKeysNames2), 'FilePermutations':new})

print(df)

print('\n')

for i, per in df.iterrows(): #desempaquetamos el resultado en 2, i y per
    images = per["FilePermutations"].split("+")
    files = per["Permutations"].split("+")

folder_name = input("Almost finished, type a name for the new NFT folder:")
final_path = os.path.join(final_output, folder_name)
while True:
    try:
       multiplier=int(input("Ok, now type an integer number you want to use as a multiplier for enlarging the image sizes:"))
       break
    except ValueError:
       print("Please, enter ONLY a positive integer number")
       continue
    else:
        break
os.mkdir(final_path)
for i, per in df.iterrows():
    images = per["FilePermutations"].split("+")
    files = per["Permutations"].split("+")
    result_image = None 

    for direc, img in zip(files, images): #iteramos
        if img=="None": continue #si es None omitimos

        path = f"{final_output}/{direc}/{img}"

        if result_image == None: 
            result_image = Image.open(f"{path}")
        else: 
            img2 = Image.open(f"{path}")
            result_image = Image.alpha_composite(result_image, img2)

    result_image = result_image.resize((result_image.size[0]*multiplier, result_image.size[1]*multiplier), resample=Image.NEAREST)
    print(f'Exporting {i}.png to: /{folder_name}/')
    result_image.save(f"{final_path}/{i}.png")
time.sleep(0.3)
print('\n')
res = pd.concat([df.Permutations.str.split('+', expand=True), df.FilePermutations.str.split('+', expand=True)], axis=1).replace({'_': ' ', '.png': ''}, regex=True) #Change the Metadata format
res.sort_index(axis=1, inplace=True)
print(f'Exporting {folder_name}_NFTs_Metadata.csv to: {final_path}')
res.to_csv(f'{final_path}/{folder_name}_NFTs_Metadata.csv')
time.sleep(0.1)
print('\n')
print('\033[0;37;42mAll done!, Thank you for using SAND-wich, built by @NoahVerner, see you next time :)\033[0m')
time.sleep(3)
