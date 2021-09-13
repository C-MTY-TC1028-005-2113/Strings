def main():
    #escribe tu código abajo de esta línea
    
    palabra = input()
    separa = int(input())
    if separa>0:
        if len(palabra) == separa:
            print(palabra)
        else:
            nueva = ""
            for i in range(0,len(palabra),separa):
                if i+separa >= len(palabra):
                    nueva += palabra[i:]
                else:
                    nueva += palabra[i:separa+i]+"-"
            print(nueva)
    else:
        print("Error")

if __name__=='__main__':
    main()
