#code by DEBIAN STAR
import os
os.system("sudo apt-get install espeak")
os.system("sudo apt-get install python3")
os.system("sudo apt-get install python3-tk")
import tkinter as tk

from espeak import espeak

os.system("sudo apt-get install nmap")
p = tk.Tk()
p.wm_title("Nmap scanner")
espeak.synth("enter I P ADDRESS")

def hello():
  os.system("sudo nmap -Pn %s"%t.get())

def site():
  os.system('firefox https://www.youtube.com/channel/UCTDlWkI2hHs4paw3JBnNLTg')

label = tk.Label(p, text="nmap scanner-debGUI\n\n ENTER IP ADDRESS",fg="green",activebackground="white",width='50',height='5')
label.pack()

t=tk.Entry(p,bd=5)
t.pack()

l=tk.Button(p,text="start scan",command=hello,bg='Blue',fg='white')
l.pack()

h=tk.Button(p,text='FOLLOW US ON YOUTUBE',command=site)
h.pack() 
p.mainloop() 
