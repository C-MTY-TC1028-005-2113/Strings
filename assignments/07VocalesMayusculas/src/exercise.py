def main():
    #escribe tu código abajo de esta línea
    
    palabra = input()
    nueva = ""
    for letra in palabra:
        if letra in "aeiou":
            nueva = nueva + letra.upper()
        else:
            nueva = nueva + letra
    print(nueva)

if __name__=='__main__':
    main()
