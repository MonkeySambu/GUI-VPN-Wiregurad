import os 
from turtle import *
import turtle
import tkinter as tk

w = 500
h = 300



def gui():
    # creo una finetra principale con tkinter
    screen = tk.Tk()
    
    # imposto le dimensioni della finestra e il il titolo
    screen.geometry(f"{w}x{h}")
    screen.resizable(False, False)
    screen.title("VPN Connection")
    
    # recupero le dimensioni dello schermo
    l_screen = screen.winfo_screenwidth()
    h_screen = screen.winfo_screenheight()
    #calcolo la posizione della finestra
    x = (l_screen/2) - (w/2)
    y = (h_screen/2) - (h/2)
    # imposto la posizione della finestra al centro dello schermo
    screen.geometry(f"+{int(x)}+{int(y)}")
    
    #creo un canvas per disegnare con turtle
    canvas= tk.Canvas(screen, width=w, height=h)
    canvas.pack()
    
    #creo un oggetto turtle per disegnare
    windows = turtle.TurtleScreen(canvas)
    windows.bgcolor("black")
    
    #Scrivo il testo
    testo= "VPN Connection"
    windows._write(txt=testo, font=("Arial", 20, "bold"), align="center",pencolor="white", pos=(0, 100))
    
    #carico le immagini
    on= tk.PhotoImage(file="assets/poweron.png")
    off= tk.PhotoImage(file="assets/poweroff.png")
    
    #creo un pulsante per la connessione
    button1= tk.Button(screen, image=on,command=lambda:vpn(True),bg="black", activebackground="#0f0f0f", border=0)
    button1.place(x=50, y=100)
    
    #creo un pulsante per la disconnessione
    button2= tk.Button(screen, image=off,command=lambda:vpn(False),bg="black", borderwidth=0)
    button2.place(x=300, y=100)
    
    def vpn ( option ) :
    # option = input("Enter 1 for VPN connection and 2 for disconnection: ")
        if option:
            os.system('nmcli connection up Samu')
            status= tk.Label(screen, text="VPN Connection successful", font=("Arial", 12), bg="black", fg="white").place(x=260, y=250)
        else:
            os.system('nmcli connection down Samu')
            status = tk.Label(screen, text="VPN Disconnection successful", font=("Arial", 12), bg="black", fg="white").place(x=260, y=250)
    
    #tengo la finestra aperta fino a quando non la chiudo
    screen.mainloop()
    

        
        
gui()
#mainloop()    
#vpn()

