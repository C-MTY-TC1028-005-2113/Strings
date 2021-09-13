def main():
    #escribe tu código abajo de esta línea
    
    palabra = input()
    palabra = palabra.lower().replace(" ", "")
   
    if palabra == palabra[::-1]:
        print("Es un palindromo")
    else:
        print("NO es un palindromo") 

if __name__=='__main__':
    main()
