import tkinter as tk
import datetime

class TelaPrincipal:
    def __init__(self, master):
        self.nossaTela = master
        self.lblRelogio = tk.Label(
            self.nossaTela, font=('Arial', 26), fg='Black')
        self.lblRelogio.pack(pady=200, padx=100)
        self.alteracao()
    def alteracao(self):
        now = datetime.datetime.now()
        self.lblRelogio['text'] = now.strftime('%H:%M:%S')
        self.nossaTela.after(1000, self.alteracao)

janelaRaiz = tk.Tk()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop()


import tkinter as tk
import mysql.connector 
from tkinter import *
  
 
def submitact():
     
    user = Username.get()
    passw = password.get()
  
    print(f"The name entered by you is {user} {passw}")
  
    logintodb(user, passw)
  
 
def logintodb(user, passw):
     
    
    
    if passw:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     password = passw,
                                     db ="College")
        cursor = db.cursor()
         
    
    
    else:
        db = mysql.connector.connect(host ="localhost",
                                     user = user,
                                     db ="College")
        cursor = db.cursor()
         
    
    savequery = "select * from STUDENT"
     
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
       
      for x in myresult:
            print(x)
        print("Query Excecuted successfully")
         
    except:
        db.rollback()
        print("Error occured")
  
 
root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")
  
 
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)
 
submitbtn = tk.Button(root, text ="Login", 
                      bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)
 
root.mainloop()