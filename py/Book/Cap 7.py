"""
from tkinter import *


def save():
    a = open("transacoes.txt", "a")
    a.write(field.get())


epe = Tk()
epe.title("Bão")
epe.geometry("1366x720")
field = Entry(epe)
service = StringVar()
service.set(None)
fieldao = Text(epe)
Radiobutton(epe, text="Marca ae", value="Marca porra", variable=service).pack()
Radiobutton(epe, text="Marcaa aee", value="n Marca porra", variable=service).pack()
Radiobutton(epe, text="Marca aeee", value="nn Marca porra", variable=service).pack()
Radiobutton(epe, text="Marcaa aae", value="n n n Marca porra", variable=service).pack()
Radiobutton(epe, text="Marca aaae", value="nnn Marca porra", variable=service).pack()
print(service.get())
service.set("Marca porra")

button = Button(epe, width=10, command=save)
field.pack(side="top"), fieldao.pack(side="bottom")
epe.mainloop()


"""
from tkinter import *


def save():
    a = open("transacoes.txt", "a")
    a.write(field.get())


epe = Tk()
epe.title("Bão")
epe.geometry("1366x720")
field = Entry(epe)
service = StringVar()
service.set(None)
fieldao = Text(epe)
"""Radiobutton(epe, text="Marca ae", value="Marca porra", variable=service).pack()
Radiobutton(epe, text="Marcaa aee", value="n Marca porra", variable=service).pack()
Radiobutton(epe, text="Marca aeee", value="nn Marca porra", variable=service).pack()
Radiobutton(epe, text="Marcaa aae", value="n n n Marca porra", variable=service).pack()
Radiobutton(epe, text="Marca aaae", value="nnn Marca porra", variable=service).pack()"""
cities = ["Marca eu", "não, Marca eu", "Eu", "Aqui"]
OptionMenu(epe, service, *cities).pack() # * pega o resto dos parâmetros
print(service.get())
service.set("Marca porra")

button = Button(epe, width=10, command=save)
field.pack(side="top"), fieldao.pack(side="bottom")
epe.mainloop()
