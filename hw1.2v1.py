"""
Filename: hw1.2v1.py
Description: This file generates encryption for caeser cypher
decrypts using key and brute force
Author: Subharthi Banerjee
Ver. : 1.2.1
Dated: 02052016
"""
import time
import sys
import string
from collections import OrderedDict
from string import digits

def encrypt(plaintext, key):
    textl = [plaintext[i: i + 1] for i in range(0, len(plaintext), 1)]  # it will make a list


    cipherl = textl
    for i in range(0, len(textl)):
        c = ord(textl[i]) - ord('A')    #check difference from 0 to 25
        eC = (c + key) %26              #encrypting
        cipherl[i] = chr(ord('A') + eC)

    ciphertext = ''.join(cipherl)
    
    return ciphertext


def decrypt(ciphertext, key):

    textl = [ciphertext[i: i + 1] for i in range(0, len(ciphertext), 1)]  # it will make a list


    plainl = textl
    for i in range(0, len(textl)):
        c = ord(textl[i]) - ord('A')    #check difference from 0 to 25
        eC = (c - key) %26              #decrypting
        plainl[i] = chr(ord('A') + eC)

    plaintext = ''.join(plainl)
    
   
    return plaintext


def bruteAttack(ciphertext):
    for k in range (0, 26):
        text = decrypt(ciphertext, k)
        print 'key = ', k, 'decrypted text: ', text      
    

def main():
    k = input('Type your key taking a value from 0 to 25 :\t')
    print 'You have chosen k = ', k
    if (k > 25 or k < 0):
        print 'Please select the key from 0-25'
        sys.exit(0)
    plaintext = raw_input('\n\n\nPlease enter your text what you want to encrypt:\t')
    text = plaintext.upper()            #upper case
    text = text.translate(None, digits)     #remove digits if any
    text = text.replace(" ", "")            # remove space if any
    text1 = text.translate(string.maketrans("",""), string.punctuation)         # remove punctuationd
    plaintext = text1               #plaintext prepared

   
    
    print 'your plaintext is now ready for processing as::::', plaintext

    print 'Starting encryption ------ \n\n'
    ciphertext = encrypt(plaintext, k)
    print 'The ciphertext is '
    print ciphertext

    print 'starting decryption------------------\n'
    plaintext = decrypt(ciphertext, k)
    print 'the plaintext is from the decryption  '
    print plaintext
    print 'starting brute force attack -----'
    print 'starting timer -----'
    sTime = time.time()
    bruteAttack(ciphertext)
    print 'Brute attack took time for deciphering: ', time.time() -  sTime, 's to run' 
    
    

## Run main


if __name__ == "__main__":
    main()


    
    

"""
Filename: hw1.2v1.py
Description: This file generates encryption for caeser cypher
decrypts using key and brute force
Author: Subharthi Banerjee
Ver. : 1.2.1
Dated: 02052016
"""
import time
import sys
import string
from collections import OrderedDict
from string import digits

def encrypt(plaintext, key):
    textl = [plaintext[i: i + 1] for i in range(0, len(plaintext), 1)]  # it will make a list


    cipherl = textl
    for i in range(0, len(textl)):
        c = ord(textl[i]) - ord('A')    #check difference from 0 to 25
        eC = (c + key) %26              #encrypting
        cipherl[i] = chr(ord('A') + eC)

    ciphertext = ''.join(cipherl)
    
    return ciphertext


def decrypt(ciphertext, key):

    textl = [ciphertext[i: i + 1] for i in range(0, len(ciphertext), 1)]  # it will make a list


    plainl = textl
    for i in range(0, len(textl)):
        c = ord(textl[i]) - ord('A')    #check difference from 0 to 25
        eC = (c - key) %26              #decrypting
        plainl[i] = chr(ord('A') + eC)

    plaintext = ''.join(plainl)
    
   
    return plaintext


def bruteAttack(ciphertext):
    for k in range (0, 26):
        text = decrypt(ciphertext, k)
        print 'key = ', k, 'decrypted text: ', text      
    

def main():
    k = input('Type your key taking a value from 0 to 25 :\t')
    print 'You have chosen k = ', k
    if (k > 25 or k < 0):
        print 'Please select the key from 0-25'
        sys.exit(0)
    plaintext = raw_input('\n\n\nPlease enter your text what you want to encrypt:\t')
    text = plaintext.upper()            #upper case
    text = text.translate(None, digits)     #remove digits if any
    text = text.replace(" ", "")            # remove space if any
    text1 = text.translate(string.maketrans("",""), string.punctuation)         # remove punctuationd
    plaintext = text1               #plaintext prepared

   
    
    print 'your plaintext is now ready for processing as::::', plaintext

    print 'Starting encryption ------ \n\n'
    ciphertext = encrypt(plaintext, k)
    print 'The ciphertext is '
    print ciphertext

    print 'starting decryption------------------\n'
    plaintext = decrypt(ciphertext, k)
    print 'the plaintext is from the decryption  '
    print plaintext
    print 'starting brute force attack -----'
    print 'starting timer -----'
    sTime = time.time()
    bruteAttack(ciphertext)
    print 'Brute attack took time for deciphering: ', time.time() -  sTime, 's to run' 
    
    

## Run main


if __name__ == "__main__":
    main()


    
    

