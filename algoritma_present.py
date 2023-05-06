import binascii
import math

class Present:
        def __init__(self,key,rounds=32):
                self.rounds = rounds
                if len(key) * 8 == 80:
                        self.roundkeys = generateRoundkeys80(string2number(key),self.rounds)
                elif len(key) * 8 == 128:
                        self.roundkeys = generateRoundkeys128(string2number(key),self.rounds)
                else:
                        raise ValueError("Key must be a 128-bit or 80-bit rawstring")
        def encrypt(self,block):
                state = string2number(block)
                for i in range (self.rounds-1):
                        state = addRoundKey(state,self.roundkeys[i])
                        state = sBoxLayer(state)
                        state = pLayer(state)
                cipher = addRoundKey(state,self.roundkeys[-1])
                return number2string_N(cipher,8)
        def decrypt(self,block):
                state = string2number(block)
                for i in range (self.rounds-1):
                        state = addRoundKey(state,self.roundkeys[-i-1])
                        state = pLayer_dec(state)
                        state = sBoxLayer_dec(state)
                decipher = addRoundKey(state,self.roundkeys[0])
                return number2string_N(decipher,8)

        def get_block_size(self):
                return 8

#        0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f
Sbox= [0xc,0x5,0x6,0xb,0x9,0x0,0xa,0xd,0x3,0xe,0xf,0x8,0x4,0x7,0x1,0x2]
Sbox_inv = [Sbox.index(x) for x in range(16)]
PBox = [0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,
        4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,
        8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,
        12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]
PBox_inv = [PBox.index(x) for x in range(64)]

def generateRoundkeys80(key,rounds):
        roundkeys = []
        for i in range(1,rounds+1): # (K1 ... K32)
                
                roundkeys.append(key >>16)
                key = ((key & (2**19-1)) << 61) + (key >> 19)
                key = (Sbox[key >> 76] << 76)+(key & (2**76-1))
                key ^= i << 15
        return roundkeys

def generateRoundkeys128(key,rounds):
        roundkeys = []
        for i in range(1,rounds+1): # (K1 ... K32)
                
                roundkeys.append(key >>64)
                key = ((key & (2**67-1)) << 61) + (key >> 67)
                key = (Sbox[key >> 124] << 124)+(Sbox[(key >> 120) & 0xF] << 120)+(key & (2**120-1))
                key ^= i << 62
        return roundkeys

def addRoundKey(state,roundkey):
        return state ^ roundkey

def sBoxLayer(state):
        output = 0
        for i in range(16):
                output += Sbox[( state >> (i*4)) & 0xF] << (i*4)
        return output

def sBoxLayer_dec(state):
        output = 0
        for i in range(16):
                output += Sbox_inv[( state >> (i*4)) & 0xF] << (i*4)
        return output

def pLayer(state):
        output = 0
        for i in range(64):
                output += ((state >> i) & 0x01) << PBox[i]
        return output

def pLayer_dec(state):
        output = 0
        for i in range(64):
                output += ((state >> i) & 0x01) << PBox_inv[i]
        return output

def string2number(i):
    val = int.from_bytes(i, byteorder='big')
    return val

def number2string_N(i, N):
    s = '%0*x' % (N*2, i)
    return binascii.unhexlify(str(s))


def padding(s):
    BLOCK_SIZE = 8
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def unpadding(s):
    return s[0:-ord(s[-1])]

def present_enkripsi(kunci,pesan):
    block = math.ceil(len(pesan)/8)
    block_pesan=[pesan[y-8:y] for y in range(8, len(pesan)+8,8)]
    kunci = kunci.encode('utf8')
    cipher = Present(kunci)
    encrypted=""
    for i in range(block):
        a_data = block_pesan[i]
        if(i==block-1):
            a_data = padding(a_data)
        buff_cipher = cipher.encrypt(a_data.encode())
        encrypted += binascii.hexlify(buff_cipher).decode('utf8')
    return encrypted

def present_dekripsi(kunci,pesan):
    block = math.ceil(len(pesan)/16)
    block_pesan=[pesan[y-16:y] for y in range(16, len(pesan)+16,16)]
    kunci = kunci.encode('utf8')
    cipher = Present(kunci)
    decrypted=""
    for i in range(block):
        enc_1=block_pesan[i]
        ciphered = binascii.unhexlify(enc_1.encode())
        decrypted_1 = cipher.decrypt(ciphered)
        decr_1 = decrypted_1.decode('utf8')
        if(i==block-1):
            decr_1 = unpadding(decr_1)
        decrypted += decr_1
    return decrypted


binascii.hexlify(encrypted_1).decode('utf8')
    

import math

class Present:
        def __init__(self,key,rounds=32):
                self.rounds = rounds
                if len(key) * 8 == 80:
                        self.roundkeys = generateRoundkeys80(string2number(key),self.rounds)
                elif len(key) * 8 == 128:
                        self.roundkeys = generateRoundkeys128(string2number(key),self.rounds)
                else:
                        raise ValueError("Key must be a 128-bit or 80-bit rawstring")
        def encrypt(self,block):
                state = string2number(block)
                for i in range (self.rounds-1):
                        state = addRoundKey(state,self.roundkeys[i])
                        state = sBoxLayer(state)
                        state = pLayer(state)
                cipher = addRoundKey(state,self.roundkeys[-1])
                return number2string_N(cipher,8)
        def decrypt(self,block):
                state = string2number(block)
                for i in range (self.rounds-1):
                        state = addRoundKey(state,self.roundkeys[-i-1])
                        state = pLayer_dec(state)
                        state = sBoxLayer_dec(state)
                decipher = addRoundKey(state,self.roundkeys[0])
                return number2string_N(decipher,8)

        def get_block_size(self):
                return 8

#        0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f
Sbox= [0xc,0x5,0x6,0xb,0x9,0x0,0xa,0xd,0x3,0xe,0xf,0x8,0x4,0x7,0x1,0x2]
Sbox_inv = [Sbox.index(x) for x in range(16)]
PBox = [0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,
        4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,
        8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,
        12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]
PBox_inv = [PBox.index(x) for x in range(64)]

def generateRoundkeys80(key,rounds):
        roundkeys = []
        for i in range(1,rounds+1): # (K1 ... K32)
                roundkeys.append(key >>16)
                key = ((key & (2**19-1)) << 61) + (key >> 19)
                key = (Sbox[key >> 76] << 76)+(key & (2**76-1))
                key ^= i << 15
        return roundkeys

def generateRoundkeys128(key,rounds):
        roundkeys = []
        for i in range(1,rounds+1): 
                roundkeys.append(key >>64)
                key = ((key & (2**67-1)) << 61) + (key >> 67)
                key = (Sbox[key >> 124] << 124)+(Sbox[(key >> 120) & 0xF] << 120)+(key & (2**120-1))
                key ^= i << 62
        return roundkeys

def addRoundKey(state,roundkey):
        return state ^ roundkey

def sBoxLayer(state):
        output = 0
        for i in range(16):
                output += Sbox[( state >> (i*4)) & 0xF] << (i*4)
        return output

def sBoxLayer_dec(state):
        output = 0
        for i in range(16):
                output += Sbox_inv[( state >> (i*4)) & 0xF] << (i*4)
        return output

def pLayer(state):
        output = 0
        for i in range(64):
                output += ((state >> i) & 0x01) << PBox[i]
        return output

def pLayer_dec(state):
        output = 0
        for i in range(64):
                output += ((state >> i) & 0x01) << PBox_inv[i]
        return output

def string2number(i):
    val = int.from_bytes(i, byteorder='big')
    return val

def number2string_N(i, N):
    s = '%0*x' % (N*2, i)
    return binascii.unhexlify(str(s))


def padding(s):
    BLOCK_SIZE = 8
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def unpadding(s):
    return s[0:-ord(s[-1])]

def present_enkripsi(kunci,pesan):
    block = math.ceil(len(pesan)/8)
    block_pesan=[pesan[y-8:y] for y in range(8, len(pesan)+8,8)]
    kunci = kunci.encode('utf8')
    cipher = Present(kunci)
    encrypted=""
    for i in range(block):
        a_data = block_pesan[i]
        if(i==block-1):
            a_data = padding(a_data)
        buff_cipher = cipher.encrypt(a_data.encode())
        encrypted += binascii.hexlify(buff_cipher).decode('utf8')
    return encrypted

def present_dekripsi(kunci,pesan):
    block = math.ceil(len(pesan)/16)
    block_pesan=[pesan[y-16:y] for y in range(16, len(pesan)+16,16)]
    kunci = kunci.encode('utf8')
    cipher = Present(kunci)
    decrypted=""
    for i in range(block):
        enc_1=block_pesan[i]
        ciphered = binascii.unhexlify(enc_1.encode())
        decrypted_1 = cipher.decrypt(ciphered)
        decr_1 = decrypted_1.decode('utf8')
        if(i==block-1):
            decr_1 = unpadding(decr_1)
        decrypted += decr_1
    return decrypted