def main():
    #escribe tu código abajo de esta línea
    import math
    a=input()
    b=input()
    ma=math.ceil(len(a)/2)
    mb=math.ceil(len(b)/2)
    print(a[0:ma]+b[mb::])
    print(a[ma::]+b[0:mb])

if __name__=='__main__':
    main()
