import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import RPi.GPIO as GPIO
import time
from time import sleep
import mysql.connector
import cv2
import time
import numpy as np
import os
from PIL import Image
import board
import busio as io
import adafruit_mlx90614
import datetime
import hashlib
import algoritma_present as present
import binascii

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setwarnings(False)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #getting screen width and height of display
        width= self.winfo_screenwidth()
        height= self.winfo_screenheight()

        #setting tkinter window size
        self.geometry("%dx%d" % (width, height))
        self.title('Aplikasi Ruang Workshop')
        self.configure(bg='light blue')

        a = Label(self, text = "INPUT KUNCI").pack(expand=True)
        input_kunci = Entry(self)
        input_kunci.pack(expand=True)

        kunci = input_kunci.get()

        #kunci = "memoryofcupawwww"
        file_cipher="cipher_input.txt"

        # place a button on the root window
        ttk.Button(self,
                text='START', 
                command=lambda: [self.present_dekripsifile(kunci, file_cipher), self.open_window(), self.servo(), self.iconify()]).pack(expand=True)     
                
        #self.destroy()                 
                

    def present_dekripsifile(self, kunci, namafile):
        f = open(namafile, 'rb')
        data_all = f.readlines()
        f.close()
        f = open(namafile.replace("cipher_",""), 'wb')
        for x in data_all:
            x=x.decode('utf-8')
            x=x.strip()
            h_plain = present.present_dekripsi(kunci,x)
            h_plain=bytes.fromhex(h_plain)
            f.write(h_plain)
            f.write("\n".encode('utf-8'))
        f.close()
        os.remove(namafile)
        print("Dekripsi File Selesai")
            
    def open_window(self):
        window = FaceRecog(self)
        window.grab_set()

    def servo(self):
        p.ChangeDutyCycle(12.5)
        time.sleep(2)




if __name__ == "__main__":
    app = App ()
    app.mainloop()