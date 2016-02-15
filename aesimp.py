### aesimp.py:  code for validating aes.pdf 
### available in the internet


import binascii
from collections import deque
import numpy as np
##message and key 128 bits

#m1 = '000102030405060708090B0A0D0C0F0E'
k1 = '5468617473206D79204B756E67204675'
m1 = '54776f204f6e65204e696e652054776f'
hex_string = k1
msg = m1
binary = bin(int(k1, 16))[2:]
binmsg = bin(int(m1, 16))[2:]

binary = int(binary, 2)
binary = format(binary, '0128b')
print '\n\n\n\nBinary key::::\t ', binary
binmsg = int(binmsg, 2)

binmsg = format(binmsg, '0128b')
print '\n\nBinary message::::\t  ', binmsg


k = list(binary)
m = list(binmsg)

## make bytes
k8 = [binary[i: i + 8] for i in range(0, len(binary), 8)]  # byte config
m8 = [binmsg[i: i + 8] for i in range(0, len(binmsg), 8)]  # it will make the pairs

print '\n\n\nkey bytes:::  ', k8
print '\n\n\nmsg bytes:::  ', m8

## create a 4x4 matrix
mpnp = np.reshape(m8, (-1, 4))
mp = mpnp.tolist()
print '\n\nprint byte array:   ', mp


## A GF with byte substitution
## make a numpy zero array and then list
## 16x16
GF = [[0] * 16] * 16
GFnp = np.reshape(GF, (-1, 16))
NF = []
print '\n\nThe GF looks like::::   \n', GF
print '\n\nThe GFnp looks like::::   \n', GFnp
for i in range(0, 16):
    for j in range(0, 16):
        temp = (str(format(i, 'x')) + str(format(j, 'x')))
        NF.append(temp)
##print '\n\nGF looks like now::: ', NF
NF = np.reshape(NF, (-1, 16))
NF = NF.tolist()
GF = NF
##print '\n\nNF:::  ', GF

#############################################
#############################################
GF = [99, 124, 119, 123, 242, 107, 111, 197 ,48, 1, 103, 43, 254, 215, 171, 118,
202 ,130, 201, 125 ,250 ,89 ,71, 240, 173, 212, 162, 175, 156, 164, 114, 192,
183 ,253, 147 ,38, 54 ,63 ,247, 204, 52 ,165, 229 ,241 ,113 ,216 ,49 ,21,
4, 199 ,35 ,195 ,24 ,150, 5 ,154, 7 ,18, 128, 226, 235 ,39, 178, 117,
9 ,131 ,44 ,26 ,27 ,110, 90, 160, 82 ,59, 214, 179, 41 ,227, 47, 132,
83 ,209, 0, 237, 32 ,252 ,177, 91 ,106 ,203 ,190 ,57, 74 ,76 ,88 ,207,
208 ,239 ,170 ,251 ,67 ,77 ,51 ,133 ,69 ,249 ,2 ,127 ,80 ,60, 159, 168,
81, 163, 64, 143 ,146 ,157 ,56 ,245 ,188 ,182, 218 ,33 ,16 ,255 ,243, 210,
205,12 ,19, 236, 95, 151 ,68 ,23 ,196,167 ,126, 61, 100 ,93, 25 ,115,
96, 129 ,79 ,220 ,34 ,42 ,144 ,136 ,70 ,238 ,184 ,20 ,222 ,94 ,11 ,219,
224, 50, 58 ,10, 73, 6 ,36 ,92 ,194, 211 ,172, 98 ,145 ,149, 228, 121,
231 ,200 ,55, 109, 141, 213 ,78 ,169 ,108 ,86 ,244 ,234, 101, 122, 174, 8,
186 ,120 ,37 ,46, 28,166 ,180 ,198, 232 ,221 ,116 ,31, 75 ,189 ,139, 138,
112, 62 ,181 ,102, 72, 3 ,246, 14, 97 ,53, 87, 185 ,134 ,193 ,29, 158,
225 ,248, 152, 17, 105, 217, 142 ,148, 155 ,30, 135 ,233, 206, 85, 40, 223,
140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45 ,15, 176 ,84, 187, 22]
R = []







RCON = [
    0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 
    0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 
    0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 
    0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 
    0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 
    0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 
    0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 
    0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 
    0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 
    0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 
    0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 
    0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 
    0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 
    0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 
    0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 
    0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d
]

for i in range (0, 256):
    temp = format(int(RCON[i]), '02x')
    R.append(temp)
RCON = R
print '\n\n\nRCON::\t', RCON

def getRconValue(n):
    return RCON[n]
def getGFValue(n):
    return GF[n]
def rotate(w):
    w = [format(x, 'x') for x in w]
    temp = w[1:] + w[:1]
    w = [int(x, 16) for x in temp]
    return w
def core(w, i):

    ## rotate left to right
    w = rotate(w)

    for i in range(4):
        w[i] = getGFValue((w[i]))
    
    w[0] = w[0] ^ int(getRconValue(i), 16)
    return w
def createRoundKey(EK8, p):
    EKnp = np.reshape(EK8[p], (-1, 4))
    
    RKey= np.zeros(shape = (4,4), dtype = int)
    #RKey = RKey.tolist()
    for i in range(0, 4):
        RKey[:, i] = EKnp[i, :]

    return RKey
def addRoundKey(state, Rkey):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= Rkey[i][j]
        
    return state

def subBytes(state):
    for i in range(4):
        for j in range(4):
           
            state[i][j] = getGFValue(int(state[i][j]))
    
    return state

def shiftRows(state):

    for i in range(0, 4):

        m = state[i]
        temp = deque(m)
        temp.rotate(-(i))
        
        A = list(temp)
        state[i] = A
    return state

print '\nGF::: ', GF

####################
Rkey032 = [binary[i: i + 32] for i in range(0, len(binary), 32)]  # byte config


Rkey0 = k8
print '\nRkey0:  ', Rkey0
Rkeyhex = []
for i in range(0, 16):
    temp = format(int(Rkey0[i] ,2), '02x')
    Rkeyhex.append(temp)
print '\n\n\nRkeyhex\t\t', Rkeyhex


n = 16 # bytes of key
b = 176 #bytes to expand

## create the state array properly
state= np.zeros(shape = (4,4), dtype = '|S8')
print mpnp
for i in range(0, 4):
    state[:, i] = mpnp[i, :]
state = state.tolist()


for i in range(0, 4):
    for j in range(0, 4):
        state[i][j] = int(state[i][j], 2)

print '\nstate:\t', state


#expnasion of the key here

## 128 to 176
Rkeydec = [int(x, 16) for x in (Rkeyhex)]
csize = 0
it = 1
#expanded key
EK = [0] * b
for i in range(0, 16):
    EK[i]  = Rkeydec[i] 

csize += 16


 ##from wikipedia key schedule

while csize < b:
    temp = EK[csize - 4 : csize]
    
    if csize % (16) == 0 :
        temp = core(temp, it)
        it += 1

    for j in range(4):
        EK[csize] = EK[csize - 16] ^ temp[j]
        csize += 1








EKhex = [format(x, '02x') for x in EK]
print 'EK::: \t', EKhex
EK8 = [EK[i: i + 16] for i in range(0, len(EK), 16)]  # byte config
Rkey = createRoundKey(EK8, 0)
print 'Rkey:\n\n  ', Rkey

Rkey = Rkey.tolist()


state = addRoundKey(state, Rkey)
statel = state
stateadd = state
##print 'state:    \n', state
##for i in range(0, 4):
##    for j in range(0, 4):
##        statehex[i][j] = format(statel[i][j], '02x')
##

##print 'After Round key\n\n',statehex

state = subBytes(state)
statesub = state

state=  shiftRows(state)
stateshift = state
statehex = state
for i in range(0, 4):
    for j in range(0, 4):
        statehex[i][j] = format(state[i][j], '02x')

print 'After shift\n\n', statehex


