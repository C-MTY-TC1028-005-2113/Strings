def main():
    #escribe tu código abajo de esta línea

    cadena = input("Dame una cadena de caracteres: ")

    minusculas = cadena.lower()

    cont = 0
    for c in range(len(cadena)):
        if cadena[c]!=minusculas[c]:
            cont = cont +1
    
    print("El número de mayúsculas en la cadena es:",cont)

if __name__=='__main__':
    main()
