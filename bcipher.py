## Block cipher
## DES model
## Feistel cipher with confusion matric for both
## key genration and plain text
## use of confusion matrix acts like a look-up table. Swapping makes
## the process little faster
## author: Subharthi Banerjee
## version: 1

from collections import deque

blkSize = 64  #bits
keySize = 128 #bits

k1 = 'ffffffffffffffffffffffffffffffff' #128 bits and all 1's secret key
binaryk1 = bin(int(k1, 16))[2:]
binaryk1 = int(binaryk1, 2)
binaryk1 = format(binaryk1, '0128b')
m1 = '0573456784fBCDEF'   #64 bits
binarym1 = bin(int(m1, 16))[2:]
binarym1 = int(binarym1, 2)
binarym1 = format(binarym1, '064b')
## confusion matrix
## the matrix helps consfusing the key array and extract a simpler version
## from it or a conversion of 128 bits to 64 bits
##PC = [5, 92, 110, 119, 6, 90, 94, 109, 115, 117, 100, 96, 3, 36,
##      122, 95, 1, 13, 71, 111, 45, 61, 28, 86, 35, 24, 34, 20,
##      112, 87, 101, 93, 114, 88, 113, 97, 106, 44, 70, 63, 107,
##      91, 42, 7, 25, 127, 105, 8, 11, 121, 31, 0, 74, 77, 76,
##      60, 30, 49, 85, 102, 33, 64, 118, 69]
PC = [61, 17, 26, 119, 112, 60, 44, 32, 102, 83, 2, 19, 103, 35, 106, 75, 48, 72, 56, 126,
      116, 77, 54, 11, 124, 122, 63, 73, 5, 33, 27, 38, 6, 37, 123, 80, 16, 7, 84, 98,
      76, 13, 49, 120, 113, 29, 105, 9, 78, 30, 79, 115, 70, 97, 82, 12, 118, 67, 10,
      40, 92, 121, 64, 125, 51, 25, 42, 34, 55, 15, 21, 8, 24, 47, 0, 3, 71, 108, 66,
      104, 86, 69, 110, 46, 74, 22, 85, 95, 41, 93, 59, 87, 58, 117, 96, 1, 43, 62,
      111, 100, 107, 90, 28, 14, 20, 94, 4, 101, 127, 68, 31, 91, 18, 23, 99, 65, 45,
      52, 81, 89, 50, 57, 114, 36, 39, 53, 88, 109]
## initial permutation matrix to confuse the plaintext

IP = [57, 17, 44, 2, 55, 7, 25, 34, 56, 30, 36, 40, 6, 21, 27,
      45, 29, 58, 35, 12, 42, 60, 53, 31, 46, 33, 3, 10, 48,
      16, 1, 47, 9, 14, 23, 13, 18, 37, 28, 61, 52, 51, 63,
      59, 24, 22, 62, 50, 38, 15, 11, 41, 43, 54, 4, 39, 32, 5, 20,
      0, 26, 19, 49, 8]

#make th ekey 32 bit before processing

PC2 = PC2 = [124, 100, 50, 118, 5, 80, 70, 56, 90, 25, 82, 28, 37, 95, 27, 24, 64, 77, 2, 67, 101, 116, 111, 122, 74, 104, 61, 23, 42, 7, 81, 32]
# confusion matrix
PC3 = [2, 20, 24, 6, 4, 25, 26, 15, 16, 27, 7, 17, 31, 3, 1, 13, 28, 22, 9, 8, 10, 21, 23, 12, 14, 11, 19, 30, 0, 18, 29, 5]
def confuseKey(key):

    CDpermute = []


    for i in range (0, len(PC)):
        m = key[PC[i]]
        CDpermute.append(m)

    key = CDpermute
    
    return key

def generateSubKey(key, nbrRound):

    ## circular left shift
    Rkeyn = deque(key)
   
    Rkeyn.rotate(-(nbrRound))
    
    Rkeyn = list(Rkeyn)
    
    Rkeyn = list(Rkeyn)
    Rkey = Rkeyn[0:32]
   
    return Rkey
def roundFunction(RKeyn, Rn, flag):

    CDpermute = []
    
   
        

    Rkn = ''.join(RKeyn)
    
    Rn = ''.join(Rn)
    ##bit wise XOR
  
    A = int(Rkn, 2) ^ int(Rn, 2)
    A = format(A, '032b')  #bit padding if needed
    
    A = list(str(A))
        

    fn = A
    fn = ''.join(fn)
    return fn


def roundEncrypt(left, right,k, n):

    temp = left
    left = right
    
    
    Rkey = generateSubKey(k, n)
   
    f = roundFunction(Rkey, right, 0)
    
    te = ''.join(temp)
    
    A = int(f, 2) ^ int(te, 2)
    A = format(A, '032b')  #bit padding if needed
   
    right = list(str(A))
   
    
    
    return [left, right]
def roundDecrypt(left, right,k, n):

    temp = left
    left = right
    
    
    Rkey = generateSubKey(k, n)
   
    f = roundFunction(Rkey, right, 1)
   
    te = ''.join(temp)
    
    A = int(f, 2) ^ int(te, 2)
    A = format(A, '032b')  #bit padding if needed
    
    right = list(str(A))
   
    
    
    return [left, right]
def encrypt(plaintext, key, nbrRound):

    permutedmsg = []
   
   
    ## left and right half of the msg for first round
    
    #check
    permutedmsg = plaintext
   
    L0 = permutedmsg[0:32]
    R0 = permutedmsg[32:64]
    
    right = R0
    left = L0
    
    keyc = confuseKey(key)
   
    for i in range(1, nbrRound + 1):
       
        [left, right] = roundEncrypt(left, right, keyc, i)
        
    
    left = ''.join(left)
    right = ''.join(right)
   
    ciphertext = right + left
   
    return ciphertext

def decrypt(ciphertext, key, nbrRound):

    LD0 = ciphertext[0 : 32]
    RD0 = ciphertext[32 : 64]
    left = LD0
    right = RD0
    keyc = confuseKey(key)
   
                
    for i in range(nbrRound, 0, -1):
        [left, right] = roundDecrypt(left, right, keyc, i)
    
    
    left = ''.join(left)
    right = ''.join(right)
   
    plaintext = right + left
    plaintext = list(plaintext)
    
   
    plaintext = ''.join(plaintext)
    return plaintext



def main():
    nbrRounds = input('Please enter the number of rounds:\t');
    
    
    k1List = list(binaryk1)
    m1List = list(binarym1)

   
    print 'Key::::::\n', k1
    print 'The message block::::::::\n', m1
    ciphertext = encrypt(m1List, k1List, nbrRounds)
    print 'ccc:  ', len(ciphertext)
    
   
    cipher = format(int(str(ciphertext), 2), '016x')
    print 'ciphertext:::   ', cipher

    ciphertext = list(str(ciphertext))
   
    
    plaintext = decrypt(ciphertext, k1List, nbrRounds)
   

    plain = format(int(str(plaintext), 2), '016x')
    print 'plaintext:\t', plain

if __name__ == "__main__":
    main()


