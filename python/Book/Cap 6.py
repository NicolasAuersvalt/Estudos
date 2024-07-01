"""
import pygame
import time

sounds = pygame.mixer
sounds.init()


def wait_finish(channel):
    while channel.get_busy():
        pass

print("Welcome aboard captain, some systems need attencion")
s = sounds.Sound("AI_welcome_attention.wav")
wait_finish(s.play())
s1 = sounds.Sound("AI_welcome.wav")
time = time.sleep(5)
print("Welcome Aboard, captain, all systems online")
wait_finish(s1.play())
s2 = sounds.Sound()



from tkinter import *

mensagem = "Aperta"
def button_click():
    mensagem = 'Mais forte'
    lab = Label(app, text=mensagem, width=50)
    b1.pack(), lab.pack()

app = Tk()
app.title("Database")
app.geometry("1366x720")
lab = Label(app, text = mensagem, width= 50)
b1 = Button(app, text="Click me!", width=10, command=button_click)
b1.pack(), lab.pack()
b1.pack(padx=10, pady=10)
app.mainloop()



def save_transaction(price, credit_card, description):
    file = open ("transactions.txt", "a")
    file.write("%16s%07%s\n" % (credit_card, price * 100, description))
    file.close()

items = ["Donuts", "Café", "Bolo", "Muffin"]
prices = [1.50, 2.0, 1.8, 1.20]
running = True

while running:
    options = 1

    for choice in items:
        print(str(options) + ". " + choice)
        options =+ int(options)
    print(str(options) + ". Quit")
    coice = int(input("Choose an option: "))

    if choice == options:
        running = False
    else:
        credit_card = input("Credit card number: ")
        save_transaction(prices[choice - 1], credit_card)

from tkinter import *

mensagem = "Aperta"
def button_click():
    mensagem = 'Mais forte'
    lab = Label(app, text=mensagem, width=50)
    b1.pack(), lab.pack()

app = Tk() # Cria uma janela chamada app
app.title("Database") # Título
app.geometry("1366x720") # Coordenadas/resolução
lab = Label(app, text = mensagem, width= 50) # Adiciona um label, fornece Texto, fornece valor de largura
b1 = Button(app, text="Click me!", width=10, command=button_click) # Command receberá true/1 quando apertado, então fará tal ação (button_click)
b1.pack(), lab.pack() # Pack é o posicionamento do botão na janela; side = left, top, right, bottom
b1.pack(padx=10, pady=10) # Eixo x and y em PIXELS!
app.mainloop() # Inicio do laço de evento Tkinter


button_one = Button(software, text = "Verificação Rápida", width = 20, command = button_clicked)
button_two = Button(software, text = "Verificação Completa", width = 20, command = button_clicked)
button_one.pack(padx = (0.01, 800), pady = (300, 100)), button_two.pack(padx = (800, 0.01), pady = (30, 10))
"""

from tkinter import *

def button_fast():
    return

def button_complete():
    return

software = Tk()
software.title("Teste")
software.geometry("1366x720")
button_one = Button(software, text = "Verificação Rápida", width = 20, command = button_fast)
button_two = Button(software, text = "Verificação Completa", width = 20, command = button_clicked)
button_one.pack(side = "left", padx = (200), pady = (200)), button_two.pack(side = "right", padx = (200), pady = (200))
software.mainloop()