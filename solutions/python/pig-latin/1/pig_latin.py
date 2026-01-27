def translate(text):
    palavras = text.lower().split()
    resultado = []
    vogais = ("a","e","i","o","u")

    for palavra in palavras:
        if palavra.startswith(("a","e","i","o","u","xr","yt")):
            resultado.append(palavra + "ay")

        else:
            i = 0
            while i <len(palavra) and palavra[i] not in vogais and not (palavra[i] == "y" and i !=0):
                if palavra[i] == "q" and i + 1< len(palavra) and palavra[i + 1] == "u":
                    i += 2
                    break
                i += 1
            resultado.append(palavra[i:] + palavra[:i] + "ay")
    return " ".join(resultado)
        