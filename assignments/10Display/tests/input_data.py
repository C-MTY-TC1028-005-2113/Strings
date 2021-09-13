# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    ( 
        ["Hola. Buenas buenas. Cómo amanecieron?"], 
        ["Dame una cadena de caracteres: ","La cadena recortada es: Hola. Buenas bu"],
        "Cuida los índices al cortar la cadena."
    ),
    ( 
        ["o"], 
        ["Dame una cadena de caracteres: ","La cadena recortada es: o"],
        "Cuida los índices al cortar la cadena."
    ),
    ( 
        ["La cadena recortada es:"], 
        ["Dame una cadena de caracteres: ","La cadena recortada es: La cadena recor"],
        "Cuida los índices al cortar la cadena."
    )
]