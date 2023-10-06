# Testar em: https://www.programiz.com/python-programming/online-compiler/
print("Atenção nas unidades!\n")

print("Digite a capacitância (F): \n")
c = float(input())

print("Digite 1° resitência (Ω): \n")
ra = float(input())

print("Digite 2° resistência (Ω): \n")
rb = float(input())


th = float(((0.6931) * (ra+rb) * c)) # TESTADO

tl = float(((0.6931)  * rb * c)) #  TESTADO

t = float(th+tl) #  TESTADO

f = float(1/t) #  TESTADO

d = float(th/t) #  Correto

print("O valor do TH é de aproximadamente: {:.3f}s\n".format(th))

print("O valor de TL é de aproximadamente: {:.3f}s\n".format(tl))

print("O valor da f é de aproximadamente: {:.3f}Hz\n".format(f))

print("O valor de T é de aproximadamente: {:.3f}v\n".format(t))

print("O valor de D é de aproximadamente: {:.3f}% \n".format(d))

print("Digite BÃO para sair: ")
a = input()
