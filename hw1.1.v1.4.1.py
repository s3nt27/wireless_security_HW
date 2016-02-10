"""
Filename: hw1.1.v1.4.1.py
Description: This file generates key matrix,
encrypts the plaintext and decrypts the cipher text with the keyword


Author: Subharthi Banerjee
Ver. : 1.4.2
version information:
Key matrix generates fine
encryption works
decryption works

Dated: 02052016

License: Please use the code freely giving the deserved credit to the authors
"""
import numpy as np
import os
import sys
import string
from collections import OrderedDict
from string import digits

print '\n\n\n\n\n\n\n'


## generates the playfair matrix with this function

def keyPreProcess(key):
    key = key.replace(" ", "")
    key = key.upper();  #change the key to uppercase

    key = ''.join([i for i in key if not i.isdigit()])
    keyArray = list(key);  # making the key as array
    # check if j & i both exists

    for i in keyArray:
        for j in keyArray:
            if (i == 'I') is True & (j == 'J') is True:
                   print 'J & I both can not coexist in the keyword'
                   sys.exit(0)
    ## keeping original order while having the key restored

    keyArray = list(OrderedDict.fromkeys(key))


            


    if type(key) is not str:
        out = 'Please choose a word as a key next time'
        print out
        sys.exit(0)


    newKey = ''.join([str(x) for x in keyArray])

    key = newKey
    out = 'You entered key as ' + key
    print out;
    # upto this point the key is generated with no
    # duplication of character
    # the keyword is now collected
    # Creating the playfair matrix

    print '\n============Starting to generate the playfair matrix===========\n'

    # create a list from A to Z
    matr = list(string.ascii_uppercase)

    # join two lists
    newKeyArray = keyArray + matr;
    newKey = ''.join([str(x) for x in newKeyArray])  # join two lists
    keyArray = list(OrderedDict.fromkeys(newKey))  # ordering the characters without duplications
    keyArray.remove('J') #removing J to consider I in the key only
    print 'Playfair matrix as an array'
    print keyArray


    n = 5
    pfm = [keyArray[i:i+n] for i in range(0, len(keyArray), n)]  # 1d to 2D transformation for print
    # pyhtonic array print
    print '\n\n\n\n\nThe playfair keyword         \n\n'
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
          for row in pfm]))

    return keyArray
########################################################################
########################################################################

# The key is created
# Next is playing with the plaintext
# input is as plain text
# cipher text will be returned
# and viceversa

########################################################################
########################################################################


def recurCheck(text):

    plaintext = text

    textl = [text[i: i + 1] for i in range(0, len(text), 1)]  # it will make the pairs
    textf = textl
    for i in range(0, len(textl) - 1, 2):
        if (textl[i] == textl[i + 1]):
          
            textf.insert(i + 1, 'X');
            plaintext = ''.join(textf)
            plaintext = recurCheck(plaintext)
            break    
        
    
    return plaintext
    
## invertible encrypt and decrypt function


# if the pairs has duplicate element remove the element with X
#  if the last element list is not a pair end with Z
# that is how we get plain text

def encrypt(plaintext, key):

    # for cipher
    textL = [plaintext[i: i + 2] for i in range(0, len(plaintext), 2)]  # it will make the pairs
    textl = [plaintext[i: i + 1] for i in range(0, len(plaintext), 1)]  # it will make the pairs
    

    print 'plain text before inserting X'
    print textL
    
    print '\n\nGenerating actual plain text\n\n'

   

            
    textf = textl

    ## put X between the pairs and check recursively
    for i in range(0, len(textl) - 1  , 2):
        if (textl[i] == textl[i + 1]):
           
            textf.insert(i + 1, 'X');
            plaintext = ''.join(textf)
            plaintext = recurCheck(plaintext)
            
            break
        
   
    
     

    
    
   

    # check if all the elements are pairable
    if (len(plaintext) % 2) is not 0:
        c = chr(ord('A') + ((ord(plaintext[len(plaintext) - 1]) - ord('A') + 1)%26))
        plaintext = plaintext + c

    textL = [plaintext[i: i + 2] for i in range(0, len(plaintext), 2)]  # it will make the pairs
    textl = [plaintext[i: i + 1] for i in range(0, len(plaintext), 1)]  # it will make the ones


    print 'Plain text After inserting X'
    print textL
    #print textL
    
    #######################################################
    #######################################################
    #encryption starts here
    ##
    #######################################################
    key5 = np.reshape(key, (-1, 5))


    print 'key in np array form\n\n'
    print key5
   
    cipherl = textl



    key = key5.tolist()
    #print textl

    
    ## encyption logic
    for i in range (0, len(textl) , 2):
        r1, c1 = np.where(key5 == textl[i])
        r2, c2 = np.where(key5 == textl[i + 1])
        
        if (r1 == r2 and c1 != c2):
            case = 1
            if (c1 == 4):
                cipherl[i] = key[r1][0]
                cipherl[i + 1] = key[r2][c2 + 1]
            elif (c2 == 4):
                cipherl[i + 1] = key[r2][0]
                cipherl[i] = key[r1][c1+1]
            else:
                cipherl[i] = key[r1][c1 + 1]
                cipherl[i + 1] = key[r2][c2 + 1]
        elif (c1 == c2 and r1 != r2):
            case = 2
            if (r1 == 4):
                cipherl[i] = key[0][c1]
                cipherl[i + 1] = key[r2 + 1][c2]
            elif (r2 == 4):
                cipherl[i + 1] = key[0][c2]
                cipherl[i] = key[r1 + 1][c1]
            else:
                cipherl[i] = key[r1 + 1][c1]
                cipherl[i + 1] = key[r2 + 1][c2]
        else:
            case =  3
            cipherl[i] = key[r1][c2]         ##change with the intersection
            cipherl[i + 1] = key[r2][c1]





    
    ciphertext = cipherl
    return ciphertext


def decrypt(ciphertext, key):

    textL = [ciphertext[i: i + 2] for i in range(0, len(ciphertext), 2)]  # it will make the pairs
    textl = [ciphertext[i: i + 1] for i in range(0, len(ciphertext), 1)]  # it will make the pairs


    #######################################################
    #######################################################
    #decryption starts here
    ##
    #######################################################
    key5 = np.reshape(key, (-1, 5))

    plainl = textl



    key = key5.tolist()
    ## decyption logic
    for i in range (0, len(textl) , 2):
        r1, c1 = np.where(key5 == textl[i])
        r2, c2 = np.where(key5 == textl[i + 1])
        
        if (r1 == r2 and c1 != c2):
            case = 1
            if (c1 == 0):
                plainl[i] = key[r1][4]
                plainl[i + 1] = key[r2][c2 - 1]
            elif (c2 == 0):
                plainl[i + 1] = key[r2][4]
                plainl[i] = key[r1][c1 - 1]
            else:
                plainl[i] = key[r1][c1 - 1]
                plainl[i + 1] = key[r2][c2 - 1]
        elif (c1 == c2 and r1 != r2):
            case = 2
            if (r1 == 0):
                plainl[i] = key[4][c1]
                plainl[i + 1] = key[r2 - 1][c2]
            elif (r2 == 0):
                plainl[i + 1] = key[4][c2]
                plainl[i] = key[r1 - 1][c1]
            else:
                plainl[i] = key[r1 - 1][c1]
                plainl[i + 1] = key[r2 - 1][c2]
        else:
            case =  3
            plainl[i] = key[r1][c2]         ##change with the intersection
            plainl[i + 1] = key[r2][c1]

    plaintext = plainl

    return plaintext





def countChar(text):

    #first collect all chars

    allChars = string.uppercase[:26]
    
    alphaList = [allChars[i: i + 1] for i in range(0, len(allChars), 1)]  # it will make the pairs
    charFreq = alphaList

    for index in range (0, len(alphaList)):
        charFreq[index] = text.count(alphaList[index])


    return charFreq


def printCountedChar(text):


    charFreq = countChar(text)
    for i in range(0, 26):
        out = chr(ord('A') + i)
        
        
        print out, charFreq[i]
    




def main():
    key = raw_input("Please enter your key to generate playfair matrix:\t")
    keyArray = keyPreProcess(key)
    plaintext = raw_input('\n\n\nPlease enter your text what you want to encrypt:\t')

   
    print 'Studying the number of character frequencies-------'

    


    

    text = plaintext.upper()
    text = text.translate(None, digits)
    print 'For plaintext -------------\n'
    printCountedChar(text)
    text = text.replace(" ", "")
    text1 = text.translate(string.maketrans("",""), string.punctuation)
    
    print '\n\n\n===================== Starting encryption =====================\n\n\n\n'
    plaintext = text1

    plaintext = plaintext.replace('J', 'I');

    ciphertext = encrypt(plaintext, keyArray)
    ciphertext = ''.join(ciphertext)

    print 'Ciphertext--------------------\n'
    print ciphertext
    textL = [ciphertext[i: i + 2] for i in range(0, len(ciphertext), 2)]  # it will make the pairs
    print '\n\nciphertext inpairs======================\n\n'
    print textL
   
    print 'For ciphertext------------------------\n'
    printCountedChar(ciphertext)

    print 'Starting decryption ---------------------------------\n\n'
    print 'Decrypted plaintext-     -----\n'
    plaintext = decrypt(ciphertext, keyArray)
    plaintext = ''.join(plaintext)
    print plaintext
    textL = [plaintext[i: i + 2] for i in range(0, len(plaintext), 2)]  # it will make the pairs
    print '\n\nplaintext in pairs======================\n\n'
    print textL

    return

## Run main


if __name__ == "__main__":
    main()

    











