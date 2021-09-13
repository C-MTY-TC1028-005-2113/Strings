![Tec de Monterrey](../../images/logotecmty.png)
# Reto Separa con Guiones

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe un programa que reciba un string y un número entero positivo, el programa crea una nueva cadena con la cadena original pero dividida con guiones en cada intervalo del número recibido y la imprime a pantalla. Si recibe un número negativo o 0, deberá imprimir el mensaje: "Error".

**Entrada:**

Un string que representa una palabra.
Un número entero positivo mayor a 0.
(Cada entrada en un renglón diferente)

**Salida:** 

La palabra recibida como entrada pero separada cada n caracteres con un guión. Si el número recibido es un número negativo o 0, se despliega el mensaje Error.


**Ejemplo de ejecución del programa:**

La salida del programa debe de ser exactamente de la siguiente forma:

```
Paracaidas
3
Par-aca-ida-s
```
```
elefante
4
elef-ante
```
```
cosa
4
cosa
```
```
elote
-2
Error
```

NOTA IMPORTANTE: Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
