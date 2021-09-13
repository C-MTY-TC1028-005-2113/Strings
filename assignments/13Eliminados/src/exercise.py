def main():
    #escribe tu código abajo de esta línea

    cadena = input("Dame una cadena de caracteres: ")
    num = int(input("Dame un número entero: "))

    nueva = ""

    for i in range(len(cadena)):
        if i%num!=0:
            nueva = nueva + cadena[i]
    
    print("La nueva cadena es:",nueva)

if __name__=='__main__':
    main()
