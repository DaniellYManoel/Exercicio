def is_armstrong_number(number):
#9 é um número Armstrong, porque 9 = 9^1 = 9
#10 não é um número Armstrong, porque 10 != 1^2 + 0^2 = 1
#153 é um número Armstrong, porque: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#154 não é um número Armstrong, porque: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
    # traforma o numero em str
    num_str = str(number)
    # Calculo a número de dígitos
    num_digits = len(num_str)
 
    armstrong_sum = 0
  
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    return armstrong_sum == number
        
