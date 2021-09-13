![Tec de Monterrey](../../images/logotecmty.png)
# Vocales Mayúsculas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe un programa, el cual recibe un string y nos despliegue como salida un nuevo string pero con todas las vocales en mayúsculas. Si la palabra no tiene vocales o las vocales ya están en mayúsculas, la salida será un String idéntico al recibido por el usuario. Para este ejercicio NO deberás utilizar la función replace de strings.

Entrada
Un string que representa una palabra o frase.

Salida
Un string como el recibido con la diferencia de que con las vocales están convertidas a mayúsculas. Si el string no contiene vocales o ya están en mayúscula, devuelve el mismo string.

**Ejemplo de ejecución del programa:**

La salida del programa debe de ser exactamente de la siguiente forma:

```
La casa azul
LA cAsA AzUl
```
```
brtdyp
brtdyp
```

**NOTA IMPORTANTE 1:** Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**NOTA IMPORTANTE 2:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.