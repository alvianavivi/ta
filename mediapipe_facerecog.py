import binascii
import os
import algoritma_present as present

def present_enkripsifile(kunci, namafile):
        f = open(namafile, 'rb')
        data_all = f.readlines()
        f.close()
        f = open("cipher_"+namafile, 'w')
        for x in data_all:
            x=binascii.hexlify(x).decode('utf-8')
            h_cipher = present.present_enkripsi(kunci,x)
            f.write(h_cipher)
            print(h_cipher)
            f.write("\n")
        f.close()
        print("Enkripsi File Selesai")

def present_dekripsifile(kunci, namafile):
        f = open(namafile, 'rb')
        data_all = f.readlines()
        f.close()
        f = open(namafile.replace("cipher_","dec_"), 'wb')
        for x in data_all:
            print(x)
            x=x.decode('utf-8')
            print(x)
            x=x.strip()
            print(x)
            h_plain = present.present_dekripsi(kunci,x)
            print(h_plain)
            h_plain=bytes.fromhex(h_plain)
            print(h_plain)
            f.write(h_plain)
            f.write("\n".encode('utf-8'))
        f.close()
        print("Dekripsi File Selesai")        


kunci = "memoryofcupawwww"
namafile1 = "cek.yml"
present_enkripsifile(kunci, namafile1)

namafile2 = "cipher_cek.yml"
present_dekripsifile(kunci, namafile2)