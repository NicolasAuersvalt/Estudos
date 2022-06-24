
"""
n = []
for m in range(100):
    n.append(m+1)
print("There are %f numbers in [1, 100]" % (5))
print("%s %e" % ("Value is", 16.0 ** 0.5))
print("%7d" % (11232/3))

"""
def transaction(price, credit_card, description):
    file = open("transacoes.txt", "a")
    file.write("%16s%07d %2s\n" % (credit_card, price * 100, description))
    # Update  file.write("%07d%16s %2s\n" % (credit_card, price * 100, description))
    file.close()

items = ["Donuts", "Café", "Bolo"]
prices = [1.50, 2.0, 2.0]
running = True

while running:
    option = 1
    for choice in items:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input("Credit card number: ")
        transaction(prices[choice - 1], credit_card, items[choice - 1])
