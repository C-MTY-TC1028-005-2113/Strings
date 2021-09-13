def main():
    #escribe tu código abajo de esta línea

    cadena = input("Dame una cadena de caracteres: ")

    recortada = cadena
    
    if "O" in cadena or "o" in cadena or "Q" in cadena:
        if len(cadena)>15:
            recortada = cadena[0:15]
    else:
        if len(cadena)>20:
            recortada = cadena[0:20]
    
    print("La cadena recortada es:",recortada)

if __name__=='__main__':
    main()
