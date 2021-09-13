![Tec de Monterrey](../../images/logotecmty.png)
# Display
Cadenas de caracteres-Display

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Modifica el programa para que haga lo siguiente:

Se tiene un dispositivo que solo puede desplegar máximo 20 caracteres. Sin embargo, si la cadena a desplegar tiene letras o, O o Q, sólo puede desplegar 15 caracteres. Realiza un programa que reciba una cadena de caracteres e imprima la cadena recortada según las capacidades del dispositivo.

Entradas: 

* Cadena de caracteres

Salida: Una cadena de caracteres que representa la cadena original recortada de acuerdo a las características de este dispositivo.

Ejemplo:

```
Dame una cadena de caracteres: Hola. Buenas buenas. Cómo amanecieron?
La cadena recortada es: Hola. Buenas bu
```

Una vez que termines tu actividad y la hayas probado con `pytest`, súbela a tu repositorio en GitHub, con el proceso de commit + push.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

[//]: # (Autor: Gil Huesca - ghjuarez at tec.mx)