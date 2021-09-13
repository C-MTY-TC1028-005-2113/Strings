def main():
    #escribe tu código abajo de esta línea

    cadena_a = input("Teclea la primer cadena de caracteres: ")
    cadena_b = input("Teclea la segunda cadena de caracteres: ")

    if len(cadena_a) > len(cadena_b):
        print(cadena_a)
    elif len(cadena_b) > len(cadena_a):
        print(cadena_b)
    else:
        print(cadena_a)
        print(cadena_b)

if __name__=='__main__':
    main()
