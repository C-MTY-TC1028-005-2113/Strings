def main():
    #escribe tu código abajo de esta línea

    cadena = input("Dame una cadena de caracteres: ")

    auxiliar = "aeiouAEIUO"

    cont = 0

    while cadena[cont] not in auxiliar:
        cont = cont+1
    
    print("El número de caracteres antes de la primera vocal es:",cont)

if __name__=='__main__':
    main()
