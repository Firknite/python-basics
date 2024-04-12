def es_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    bajando = len(texto) - 1
    subiendo = 0

    while bajando > 0:
        if texto[subiendo] != texto[bajando]:
            return False
        bajando -= 1
        subiendo += 1

    return True


print("reconocer", es_palindromo("reconocer"))
print("abba", es_palindromo("abba"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Esto no es un palindromo", es_palindromo("Esto no es un palindromo"))
