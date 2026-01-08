def steps(n):
    # n for par, divida n por 2 para obter n/2.
    # n for ímpar, multiplique n por 3 e adicione 1 para obter 3n + 1
    if n <= 0:
        raise ValueError("Only positive integers are allowed")
    s = 0
    while n != 1:
        if n % 2 ==0:
            n = n//2
        else:
            n = (n * 3) + 1
        s +=1
    return s