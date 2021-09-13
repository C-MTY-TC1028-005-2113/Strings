def main():
    #escribe tu código abajo de esta línea

    dia = input("Dame el día: ")
    mes = input("Dame el mes: ").lower()
    anio = input("Dame el año: ")

    d = dia
    if len(dia)==1:
        d = "0"+dia
    elif len(dia)==0:
        d = "00"
    elif len(dia)>2:
        d = dia[len(dia)-2:]

    m = "01"
    if mes=="enero":
        m = "01"
    elif mes=="febrero":
        m = "02"
    elif mes=="marzo":
        m = "03"
    elif mes=="abril":
        m = "04"
    elif mes=="mayo":
        m = "05"
    elif mes=="junio":
        m = "06"
    elif mes=="julio":
        m = "07"
    elif mes=="agosto":
        m = "08"
    elif mes=="septiembre":
        m = "09"
    elif mes=="octubre":
        m = "10"
    elif mes=="noviembre":
        m = "11"
    elif mes=="diciembre":
        m = "12"

    a = anio
    if len(a)==1:
        a = "0"+anio
    elif len(anio)==0:
        a = "00" 
    elif len(anio)>2:
        a = anio[len(anio)-2:]

    fecha = d+"/"+m+"/"+a
    
    print("La fecha es:",fecha)

if __name__=='__main__':
    main()
