def main():
    #escribe tu código abajo de esta línea
    
    cadena = input()
    lista = list(cadena)
    for i in range(len(lista)):
        if lista[i] in "eéÉE":
            lista[i] = "3"
        elif lista[i] in "aáÁA":
            lista[i] = "4"
        elif lista[i] in "oóÓO":
            lista[i] = "h"
    cadena = "".join(lista)
    print(cadena)

if __name__=='__main__':
    main()
