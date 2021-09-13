def main():
    #escribe tu código abajo de esta línea

    cadena = input("Teclea una cadena de caracteres: ") 

    longitud=len(cadena)
    print(longitud)
    print(cadena[0])
    print(cadena[-1])
    print(cadena[1::2])

if __name__=='__main__':
    main()
