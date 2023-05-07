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
import mediapipe as mp
import datetime

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setwarnings(False)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        global kunci

        #getting screen width and height of display
        width= self.winfo_screenwidth()
        height= self.winfo_screenheight()

        #setting tkinter window size
        self.geometry("%dx%d" % (width, height))
        self.title('Aplikasi Ruang Workshop')
        self.configure(bg='light blue')

        a = Label(self, text = "").pack(pady=80)
        a = Label(self, text = "INPUT KUNCI").pack(pady=10)
        input_kunci = Entry(self)
        input_kunci.pack(pady=2)

        kunci = input_kunci.get()

        #kunci = "memoryofcupawwww"
        file_cipher="cipher_trainer.yml"

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
            #f.write("\n".encode('utf-8'))
        f.close()
        os.remove(namafile)
        print("Dekripsi File Selesai")
            
    def open_window(self):
        window = FaceRecog(self)
        window.grab_set()

    def servo(self):
        p.ChangeDutyCycle(12.5)
        time.sleep(2)

class FaceRecog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        global id
        global names
        
        mydb = mysql.connector.connect(host = "localhost", user = "root", password = "password", database = "workshop")
        mycursor = mydb.cursor()
        sql = "select nama from identitas"
        mycursor.execute(sql)
        face_list = mycursor.fetchall()
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer.yml')

        font = cv2.FONT_HERSHEY_SIMPLEX

        id = 0

        names = face_list
        #print(face_list)
        names = [x[0] for x in names]
        
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height

        face_detection = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)
        
        status = 0
        while True:

            ret, img =cam.read()
            if not ret:
                print("kosong")
                continue

            img = cv2.flip(img, 1) # Flip vertically
            image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image_rgb)

            if results.detections:
                for detection in results.detections:
                    # Get the bounding box of the face
                    bbox = detection.location_data.relative_bounding_box
                    height, width, _ = img.shape
                    x, y, w, h = int(bbox.xmin * width), int(bbox.ymin * height), int(bbox.width * width), int(bbox.height * height)

                    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

                    face_img = img[y:y+h, x:x+w]
                    face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

                    id, confidence = recognizer.predict(face_img)

                    # Check if confidence is less them 100 ==> "0" is perfect match 
                    if (confidence < 100):
                        sql = "select role from identitas where id_user = %s"
                        mycursor.execute(sql,[(id)])
                        role_list = [x[0] for x in mycursor.fetchall()]
                        print("ID List = " + str(role_list))

                        if(len(role_list ) >= 1):
                            role = role_list[0]
                            print("Nilai role = " + str(role))
                            warna = (0,0,255)
                        else:
                            role = 'Unknown'
                            #id = names[id]
                            confidence = "  {0}%".format(round(100 - confidence))
                            #print (id)
                    else:
                        role = "Unknown"
                        confidence = "  {0}%".format(round(100 - confidence))
                    
                    now = datetime.datetime.now()
                    formatted_date = now.strftime("%Y-%m-%d %H:%i:%s")

                    mycursor1 = mydb.cursor()
                    sql2 = "select id_user from reservasi where waktu = %s"         
                    mycursor1.execute(sql2,[(formatted_date)])
                    id_list = [x[0] for x in mycursor1.fetchall()]

                    print("Nilai id reservasi = " + str(id_list))

                    if(len(id_list) >= 1):
                        id = id_list[0]
                        print("Nilai id = " + str(id))
                        warna = (0,0,255)
                        cv2.putText (img,'Pengguna Reservasi',
                                            (x+100,y+h-100), font, 1, warna, 1)
                        status = 1
                    else:
                        warna = (0,0,255)
                        cv2.putText (img,'Pengguna Tidak Reservasi!!!!',
                                            (x+100,y+h-100), font, 1, warna, 1)
                        status = 0

                    sql = "select nama from identitas where id_user = %s"
                    mycursor.execute(sql,[(id)])
                    namaa = [x[0] for x in mycursor.fetchall()]
                    nama = namaa[0]

                    cv2.putText(img, str(nama), (x+5,y-5), font, 1, (255,255,255), 2)
                    #cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
                                    
            cv2.imshow('Scan Wajah',img) 
            print(status)
            cv2.waitKey(5000) #& 0xff # Press 'ESC' for exiting video
            if (role == "admin"):
                print(role)
                self.open_window()
                break
            elif (role == "Unknown"):
                print(role)
                messagebox.showinfo("showinfo", "Anda Bukan Admin!")
                break
            elif(status == 1):
                print(id)
                self.servo()
                self.sendtoMySQL()
                
        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()
    
    
    def open_window(self):
        window = MenuAdmin(self)
        window.grab_set()

    def servo(self):
        p.ChangeDutyCycle(1.5)
        time.sleep(2)
        p.ChangeDutyCycle(12.5)
        time.sleep(2)
        
    def sendtoMySQL(self):
        id_user = str(id)
        waktumasuk = str(datetime.datetime.now())     
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="workshop"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO aksesmasuk values ('"+ id_user +"','"+ waktumasuk +"')"
        mycursor.execute(sql)

        mycursor.execute("commit")
                
class MenuAdmin(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        width= self.winfo_screenwidth()
        height= self.winfo_screenheight()
        #setting tkinter window size
        self.geometry("%dx%d" % (width, height))
        self.title('Aplikasi Admin')
        self.configure(bg='pink')

        ttk.Button(self,
                text='Login',
                command=lambda: [self.sendtoMySQL(), self.servo(), self.open_window2()]).pack(expand=True)
        ttk.Button(self,
                text='Register',
                command=lambda: [self.open_window(), self.iconify()]).pack(expand=True)
        
       
    def servo(self):
            p.ChangeDutyCycle(1.5)
            time.sleep(2)
            p.ChangeDutyCycle(12.5)
            time.sleep(2)
            
    def open_window2(self):
        window = FaceRecog(self)
        window.grab_set()
                   
    def sendtoMySQL(self):
        id_user = str(id)
        waktumasuk = str(datetime.datetime.now())     
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="workshop"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO aksesmasuk values ('"+ id_user +"','"+ waktumasuk +"')"
        mycursor.execute(sql)

        mycursor.execute("commit")
        
    def open_window(self):
        window = InputID(self)
        window.grab_set()
        
class InputID(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        global faceface
        global facename
        global facenpm
        global faceprodi
        global facejk
        global facenotelp
        global faceuname
        global facepw
        global facerole
        
        width= self.winfo_screenwidth()
        height= self.winfo_screenheight()
        #setting tkinter window size
        self.geometry("%dx%d" % (width, height))
        self.title('Input ID')
        self.configure(bg='light blue')

        a = Label(self, text = "ID").grid(row = 0,column = 0)
        faceface = Entry(self)
        faceface.grid(row = 0,column = 1)
        
        b = Label(self, text = "Name").grid(row = 2,column = 0)
        facename = Entry(self)
        facename.grid(row = 2,column = 1)
        
        c = Label(self, text = "NPM/NIP").grid(row = 3,column = 0)
        facenpm = Entry(self)
        facenpm.grid(row = 3,column = 1)
        
        d = Label(self, text = "Prodi").grid(row = 4,column = 0)
        options_prodi = ['RKS', 'RPK', 'RK']
        faceprodi= tk.Combobox(self, values=options_prodi)
        faceprodi.grid(row = 4,column = 1)
        
        e = Label(self, text = "Jenis Kelamin").grid(row = 5,column = 0)
        options_jk = ['L', 'P']
        facejk = tk.Combobox(self, values=options_jk)
        facejk.grid(row = 5,column = 1)
        
        f = Label(self, text = "Nomor Telepon").grid(row = 6,column = 0)
        facenotelp = Entry(self)
        facenotelp.grid(row = 6,column = 1)
        
        g = Label(self, text = "Username").grid(row = 7,column = 0)
        faceuname = Entry(self)
        faceuname.grid(row = 7,column = 1)
        
        h = Label(self, text = "Password").grid(row = 8,column = 0)
        facepw = Entry(self)
        facepw.grid(row = 8,column = 1)
        
        i = Label(self, text = "Role").grid(row = 9,column = 0)
        options_jk = ['admin', 'owner', 'user']
        facerole = Entry(self)
        facerole.grid(row = 9,column = 1)
        #lambda: [self.open_window(), self.servo()]).pack(expand=True)
        
        tk.Button(self,text='Submit', command= lambda: [self.open_window(), self.sendtoMySQL(), self.iconify()]).grid(row = 10,column = 1)
  
    def open_window(self):
        window = InputWajah(self)
        window.grab_set()
        
    def sendtoMySQL(self):
        face_id = faceface.get()
        face_name = facename.get()
        face_npm = facenpm.get()
        face_prodi = faceprodi.get()
        face_jk = facejk.get()
        face_notelp = facenotelp.get()
        face_uname = faceuname.get()
        face_pw = facepw.get()
        face_role = facerole.get()
        #print(face_name)
        
        hash_pw = hashlib.md5(face_pw.encode("utf-8")).hexdigest() 
     
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="workshop"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO identitas (id_user, nama, username, npm_nip, prodi, jk, no_telp, pass, role) VALUES (%s, %s, %s, %s, %s, %s)"        
        val = (face_id, face_name, face_uname, face_npm, face_prodi, face_jk, face_notelp, hash_pw, face_role)
        mycursor.execute(sql, val)
        
        mydb.commit()

class InputWajah(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x200')
        self.title('Input Wajah')
        self.configure(bg='pink')
        
        import cv2
        import os

        cap = cv2.VideoCapture(0)
        cap.set(3, 640) # set video width
        cap.set(4, 480) # set video height

        face_detection = mp.solutions.face_detection.FaceDetection(model_selection=1,min_detection_confidence=0.5)

        # For each person, enter one numeric face id
        face_id = faceface.get()#input('\n enter user id end press <return> ==>  ')
        

        print("\n [INFO] Initializing face capture. Look the camera and wait ...")
        # Initialize individual sampling face count
        count = 0

        while(True):

            ret, img = cam.read()
            img = cv2.flip(img, 1) # flip video image vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite('/home/pi/FaceRecog/dataset/User.' + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

                cv2.imshow('image', img)

            k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            elif count >= 30: # Take 30 face sample and stop video
                self.open_window()
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()
        
    def open_window(self):
        window = TombolTrain(self)
        window.grab_set()
        


if __name__ == "__main__":
    app = App ()
    app.mainloop()