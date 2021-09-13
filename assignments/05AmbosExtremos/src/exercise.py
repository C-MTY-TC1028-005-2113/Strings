def main():
    #escribe tu código abajo de esta línea
    s=input()
    if len(s)<2:
        resultado=''
    else:
        resultado=s[0]+s[1]+s[len(s)-2]+s[len(s)-1]
    print(resultado)


if __name__=='__main__':
    main()
