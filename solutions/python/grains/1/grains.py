def square(number):
    # 64 quadrados n = number
    #total_number =  total = 1 * ((1-(2**number)/(1-2))
    if number < 1 or number > 64: # pra ver se tá no intevalo de tempo
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)
  # Cálculo dos grãos no quadrado específico

def total():
    #total = 1 * ((1-(2**64)/(1-2))
    #return total
    return sum(square(i) for i in range(1, 65)) 
# vai chamar a primeira função 
# ela vai fazer a contar 64 vez 
# o sum vai somar todos os resultados 
# dando assim o valor total