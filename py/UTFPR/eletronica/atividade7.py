print("Digite a capacitância: \n")
c = float(input())

print("Digite 1° resitência: \n")
ra = float(input())

print("Digite 2° resistência: \n")
rb = float(input())


th = ((0.6931) * (ra+rb) * c) # Correto

tl = ((0.6931)  * rb * c) #  Correto

t = th+tl #  Correto

f = (1/t) #  Correto

d = (th/t) #  Correto

print("O valor do TH é de: {:.3f}s\n".format(th))

print("O valor de TL é: {:.3f}s\n".format(tl))

print("O valor da f é: {:.3f}s\n".format(f))

print("O valor de T é: {:.3f}v\n".format(t))

print("O valor de D é: {:.3f}% \n".format(d))
