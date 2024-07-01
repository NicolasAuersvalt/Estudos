from tkinter import *
import tkinter.messagebox

ativado = False
approved = "Chave Incorreta"
inserida = r"C:\Users\nicol\Desktop\Antivirus\Ativação\chave_inserida.txt"

def ativacao():
    print("Testando chave...")
    try:
        key_true = open(r"C:\Users\nicol\Desktop\Antivirus\Ativação\chaves_geradas.txt", "r")
        my_key = open(inserida, "r")
        key_trueRead = str(key_true.read())
        my_keyRead = str(my_key.read())
    except:
        tkinter.messagebox.showerror("ErroR", "Can't read %s \n" % inserida)

    print("Minha chave é: {}".format(my_keyRead))
    print("Chaves: {}".format(key_trueRead))
    if key_trueRead.find(my_keyRead) != -1:
        approved = "Chave Ativada com Sucesso :D"
        telaA = Tk()
        telaA.title(approved)
        telaA.geometry("400x300")
        Label(telaA, text=approved).pack()
        my_key.close()
        key_true.close()
        telaA.mainloop()
    else:
        approved = "A Chave não foi ativada D:"
        telaA = Tk()
        telaA.title(approved)
        telaA.geometry("400x300")
        Label(telaA, text=approved).pack()
        my_key.close()
        key_true.close()
        telaA.mainloop()

