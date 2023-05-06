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
            f.write("\n")
        f.close()
        os.remove(namafile)
        print("Enkripsi File Selesai")

kunci = "adekmzrk"
namafile = "trainer.yml"
present_enkripsifile(kunci, namafile)