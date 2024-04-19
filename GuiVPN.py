import os
import pygame as pg


h=300
w=500

def vpn(option):
    if option == '1':
        os.system('nmcli connection up Samu')
        print("VPN connection successful")
    elif option == '2':
        os.system('nmcli connection down Samu')
        print("VPN disconnection successful")

def gui():
    #creo la finestra principale
    pg.init()
    screen = pg.display.set_mode((w,h))
    screen.fill((0,0,0))
    pg.display.set_caption("VPN Connection")
    
    #creo un font per scrivere il testo
    font = pg.font.Font(None, 36)
    #scrivo sullo schermo
    text = font.render("VPN Connection", True, (255,255,255))
    screen.blit(text, (w//2-100, 100))
    
    #creo un pulsante per la connessione
    button1 = pg.Rect(100,200,100,50)
    pg.draw.rect(screen, (255,0,0), button1)
    font = pg.font.Font(None, 24)
    text = font.render("Connect", True, (255,255,255))
    screen.blit(text, (110,210))
    
    #creo un pulsante per la disconnessione
    button2 = pg.Rect(300,200,100,50)
    pg.draw.rect(screen, (255,0,0), button2)
    font = pg.font.Font(None, 24)
    text = font.render("Disconnect", True, (255,255,255))
    screen.blit(text, (310,210))
    
    #aggiorno lo schermo
    pg.display.flip()
    
    #ciclo principale
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    vpn('1')
                if button2.collidepoint(event.pos):
                    vpn('2')
        pg.display.flip()
        
    pg.quit()
    
gui()