import random

char = "abcdefghijklopqorstuvwxyzABCDEFGHIJKLMNOPQRSTUVHXYZ123456789@#$%!:"

while True:
        try:
                len = int(input("tamanho da senha: "))
                qty = int(input("Quantidades de senhas:"))
        except ValueError:
                print("entrada invalida")
        else:
                for x in range(0,qty):
                        passwd = ""
                        for x in range(0,len):
                                passchar = random.choice(char)
                                passwd = passwd + passchar
                        print(f"Senha gerada: {passwd}")
        break
                
