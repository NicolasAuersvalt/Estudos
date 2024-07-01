"""
Classes

class Dog():
    def __init__(self, age, name):
        #__init__ é um método. Uma função que faz parte de uma classe é um método. Essa é uma nova instância
        self.name = name
        # self é uma referência a própria instância, OBRIGATÓRIO
        # Qualquer variável prefixada com self ESTÁ DISPONÍVEL PARA TODOS OS MÉTODOS DA CLASSE e podemos...
        # ... acessar de qualquer instância a partir da classe self.name = name
        # Esse valor name atribuido a self.name é, resumindo, o valor do parâmetro sendo atribuído
        # a variável name e associado à instância

        # Essas variáveis são chamadas ATRIBUTOS







#calculadora.py
class Calculadora:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

c = Calculadora(1, 128)
print(c.soma())



# Informa o Restaurante e o tipo de Cozinha.

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.nome = restaurant_name
        self.cozinha = cuisine_type

    def describe_restaurant(self):
        return ("Nome do restaurante é: {} \nTipo de cozinha é: {}").format(self.nome, self.cozinha)


primeiro_restaurante = Restaurant("Tchê", "Inox")
segundo_restaurante = Restaurant("Boca do Forno", "Tijolo")
terceiro_restaurante = Restaurant("Dois Irmãos", "Inox Blindado")
print(primeiro_restaurante.describe_restaurant())
print(" ")
print(segundo_restaurante.describe_restaurant())
print(" ")
print(terceiro_restaurante.describe_restaurant())



class User:

    def __init__(self, first_name, last_name, senha, idade):
        self.first = first_name
        self.last = last_name
        self.passw = senha
        self.age = idade

    def describe_user(self):
        nome = ("O usuário {} {}, de {} anos, adicionou a senha: {}".format(self.first, self.last, self.age, self.age))
        return nome

    def greet_user(self):
        msg = ("Boas vindas, {}, estamos ansiosos para lhe oferecer os melhores serviços.".format(self.first))
        return msg

usr_1 = User("Amanda", "Joaquina", "Oasl2039", "20")
usr_2 = User("Nícolas", "Auersvalt", "sakn2OaA", "18")
usr_3 = User("Paulo", "Laminski", "ask3o19aZ", "24")
print(usr_1.describe_user() + "\n" + usr_1.greet_user())
print(" ")
print(usr_2.describe_user() + "\n" + usr_2.greet_user())
print(" ")
print(usr_3.describe_user() + "\n" + usr_3.greet_user())
print(" ")
"""









