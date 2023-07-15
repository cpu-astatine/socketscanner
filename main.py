# Tkinter Projects : Socket Scanner
# Programmer       : cpu-astatine
# Date             : 15.07.2023

import tkinter as tk
import subprocess 
import os
import time

os.system("clear")

pencere = tk.Tk()
pencere.geometry("500x200")
pencere.title("Socket Scanning")

def nmap():
    host = text1.get("1.0", "end-1c")
    subprocess.run(['nmap', f'{host}'])
    print("NMAP scan is complete")
    print("\n")

def angryScan():
    print("Please be patient...")
    time.sleep(1)
    host = text1.get("1.0", "end-1c")
    subprocess.run(['nmap', f'{host}', '-A', '-sT', 'sU', '-T4', 'sS'])
    print("NMAP scan is complete")

def tcpScan():
    print("Please be patient...")
    time.sleep(1)
    host = text1.get("1.0", "end-1c")
    subprocess.run(['nmap', f'{host}', '-sT'])

def quit():
    pencere.quit()

label1 = tk.Label(pencere, text="Socket Scanning")
label1.pack()

label2 = tk.Label(pencere, text="Please input the host or IP address")
label2.pack()

text1 = tk.Text(pencere, height=1, width=20)
text1.pack()

button1 = tk.Button(pencere, text="NMAP Scan", command=nmap)
button1.pack()

button2 = tk.Button(pencere, text="Angry Scan", command=angryScan)
button2.pack()

button3 = tk.Button(pencere, text="TCP Scan", command=tcpScan)
button3.pack()

button4 = tk.Button(pencere, text="QUIT", command=quit)
button4.pack()

pencere.mainloop()
