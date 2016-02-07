
## implementing one round DES
## following http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
## Author: Subharthi Banerjee


import binascii
from collections import deque
hex_string = '133457799BBCDFF1'
msg = '0123456789ABCDEF'
binary = bin(int(hex_string, 16))[2:]
binmsg = bin(int(msg, 16))[2:]

#binary = '0000000100100011010001010110011110001001101110101101110011111110'

PC1 = [57, 49, 41, 33, 25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
## S-BOX

S1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
S2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
S3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
S4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
S5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
S6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
S7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
S8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]


## expansion bit
E_bit = [32, 1, 2, 3, 4, 5,4, 5, 6, 7, 8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

##last permutation for final stage
Pf = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

binary = int(binary, 2)
binary = format(binary, '064b')
print 'Binary key: ', binary
binmsg = int(binmsg, 2)

binmsg = format(binmsg, '064b')
print 'Binary message  ', binmsg
hex_string = hex(int(binary, 2))
print hex_string
binList = [binary[i: i + 1] for i in range(0, len(binary), 1)]  # it will make the pairs
binmsgList = [binmsg[i: i + 1] for i in range(0, len(binmsg), 1)]  # it will make the pairs
binListRev = binList[::-1]
bindash = ''.join(binListRev)
print bindash
bin4 = [binary[i: i + 4] for i in range(0, len(binary), 4)]  # it will make the pairs

print bin4
#print 'Binary: ', binList
L0 = []
R0 = []

L0 = binmsgList[0:32]
R0 = binmsgList[32:64]

        

##L0 = L0[::-1]
##
##
##
##R0 = R0[::-1]
L0 = ''.join(L0)
R0 = ''.join(R0)

print 'L0 = ', L0
print 'R0 = ', R0

print 'hexadecimal       ====='
L4 = [L0[i: i + 4] for i in range(0, len(L0), 4)]  # it will make the pairs
R4 = [R0[i: i + 4] for i in range(0, len(R0), 4)]  # it will make the pairs
print L4
print R4
L0 = hex(int(L0, 2))
R0 = hex(int(R0, 2))

print 'L0 = ', L0
print 'R0 = ', R0

print 'the keys after PC1   '
key = []
for i in range (0, len(PC1)):
    m = binList[PC1[i] - 1]
    key.append(m)

##key = key[::-1]
key = ''.join(key)
print key
key4 = [key[i: i + 7] for i in range(0, len(key), 7)]  # it will make the pairs
print key4


# cutting two halves


C0 = key[0:28]
D0 = key[28:56]

print 'C0: ', C0
print 'D0: ', D0

## left circular shift

Cshift = deque(C0)
Dshift = deque(D0)

Cshift.rotate(-1)
Dshift.rotate(-1)

C1 = list(Cshift)
D1 = list(Dshift)
C1 = ''.join(C1)
D1 = ''.join(D1)
print 'C1: ', C1
print 'D1: ', D1
CD = C1 + D1
## apply permutation PC2
CD7 = [CD[i: i + 7] for i in range(0, len(CD), 7)]  # it will make the pairs
print 'CD7 ', CD7
CDpermute = []


for i in range (0, len(PC2)):
    m = CD[PC2[i] - 1]
    CDpermute.append(m)


CDpermute = ''.join(CDpermute)
K1 = CDpermute 
print 'K1   ', CDpermute
Ksub1 = [CDpermute[i: i + 4] for i in range(0, len(CDpermute), 4)]  # it will make the pairs
print 'The key after PC2'
print 'K1-4   ', Ksub1

##initial permutation of the message
permutedmsg = []
for i in range (0, len(IP)):
    m = binmsg[IP[i] - 1]
    permutedmsg.append(m)
binmsg4 = [binmsg[i: i + 4] for i in range(0, len(binmsg), 4)]  # it will make the pairs
print 'msg: ', binmsg4
permutedmsg = ''.join(permutedmsg)
permutedmsg4 = [permutedmsg[i: i + 4] for i in range(0, len(permutedmsg), 4)]  # it will make the pairs
print 'IP: ', permutedmsg4

L0 = permutedmsg[0:32]
R0 = permutedmsg[32:64]


L1 = R0  #exchange
L4 = [L0[i: i + 4] for i in range(0, len(L0), 4)]  # it will make the pairs
R4 = [R0[i: i + 4] for i in range(0, len(R0), 4)]  # it will make the pairs
print 'L0: after IP::::   ',L4
print 'R0:  after IP::::   ',R4
R0List = [R0[i: i + 1] for i in range(0, len(R0), 1)]  # it will make the pairs
E_R0 = []
## using expansion bit
for i in range(0, len(E_bit)):
    m = R0List[E_bit[i] - 1]
    E_R0.append(m)

E_R0 = ''.join(E_R0)
Blocks = [E_R0[i: i + 6] for i in range(0, len(E_R0), 6)]  # it will make the pairs
print 'E(R0):   ', Blocks

A = int(E_R0, 2) ^ int(K1, 2)
A = format(A, '048b')

print 'A: ', A
Blocks = [A[i: i + 6] for i in range(0, len(A), 6)]  # it will make the pairs
print 'Blocks:  ', Blocks
    
### S-Box processing

B_B = []
for i in range (0, len(Blocks)):
    B = Blocks[i]


    row = int(B[0] + B[5], 2)
    col = int(B[1:5],2)

    if (i == 0):
        S1_B = S1[row][col]

        S1B = format(S1_B, '04b')
        B_B.append(S1B)
        
    if (i == 1):    
        S2_B = S2[row][col]

        S2B = format(S2_B, '04b')
        B_B.append(S2B)
    if (i == 2):
            
        S3_B = S3[row][col]

        S3B = format(S3_B, '04b')
        B_B.append(S3B)
    if (i == 3):
            
        S4_B = S4[row][col]

        S4B = format(S4_B, '04b')
        B_B.append(S4B)
    if (i == 4):
            
        S5_B = S5[row][col]

        S5B = format(S5_B, '04b')
        B_B.append(S5B)
    if (i == 5):
            
        S6_B = S6[row][col]

        S6B = format(S6_B, '04b')
        B_B.append(S6B)
    if (i == 6):
            
        S7_B = S7[row][col]

        S7B = format(S7_B, '04b')
        B_B.append(S7B)
    if (i == 7):
            
        S8_B = S8[row][col]

        S8B = format(S8_B, '04b')
        B_B.append(S8B)

f = []
BB = ''.join(B_B)
BB1 = [BB[i: i + 1] for i in range(0, len(BB), 1)]  # it will make the pairs
BB4 = [BB[i: i + 4] for i in range(0, len(BB), 4)]  # it will make the pairs
print 'BB:  ', BB4

for i in range (0, len(BB1)):
    t = BB1[Pf[i] - 1]
    f.append(t)

f =''.join(f)
f4 = [f[i: i + 4] for i in range(0, len(f), 4)]  # it will make the pairs
print 'f:   ', f4

R1 = int(L0, 2) ^ int(f, 2)
R1 = format(R1, '032b')
R4 = [R1[i: i + 4] for i in range(0, len(R1), 4)]  # it will make the pairs
L4 = [L1[i: i + 4] for i in range(0, len(L1), 4)]  # it will make the pairs
print 'R1:   ', R4
print 'L1:   ', L4
L1hex = hex(int(L1, 2))
R1hex = hex(int(R1, 2))
print 'L1 in hex: ', L1hex
print 'R1 in hex: ', R1hex

cipher = R1 + L1
cipher4 = [cipher[i: i + 8] for i in range(0, len(cipher), 8)]  # it will make the 8 bits
print 'cipher after first round:  ', cipher4
print 'cipher in hex:  ', hex(int(cipher, 2))


        
        


