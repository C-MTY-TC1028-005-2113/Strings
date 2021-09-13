# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [

        ( 
            ["Paracaidas", "3"],
            ["", "", "Par-aca-ida-s"],
            "Revisa que tus datos de entrada y salida sean exactamente igual a los indicados en el README"
        ),
        ( 
            ["elefante", "4"],
            ["", "", "elef-ante"],
            "Revisa que tus datos de entrada y salida sean exactamente igual a los indicados en el README"
        ),
        (
            ["cosa", "4"],
            ["", "", "cosa"],
            "Revisa que tus datos de entrada y salida sean exactamente igual a los indicados en el README"
        ),
        (
            ["elote", "-2"],
            ["", "", "Error"],
            "Revisa que tus datos de entrada y salida sean exactamente igual a los indicados en el README"
        )
]