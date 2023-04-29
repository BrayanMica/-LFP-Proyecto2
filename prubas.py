texto = ["Hola!", "Este es un ejemplo", "de cómo usar el ciclo while", "", "para recorrer una lista línea por línea."]

index = 0 # Establecemos el índice en 0

while texto[index] != "": # Mientras la línea actual no sea vacía
    print(texto[index]) # Imprimimos la línea actual
    index += 1 # Aumentamos el índice para avanzar a la siguiente línea

print("Fin del programa") # Cuando se alcanza la línea vacía, el ciclo termina y se imprime este mensaje
