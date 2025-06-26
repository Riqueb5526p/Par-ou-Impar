parar = 0
while parar != 1:
    numero = int(input("Digite um número e descubra se é par ou impar \nOu digite 0 para parar: "))

    if numero == 0:
        parar = 1
        
    if numero % 2 == 0:
        print (f"O número {numero} é par.")

    

    else:
        print (f"O número {numero} é impar")

