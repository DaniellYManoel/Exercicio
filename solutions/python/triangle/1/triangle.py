def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a > 0:
        if a == b and b == c:     
            return True
    return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a > 0:
        if a+ b >= c and b+ c >= a and a + c >= b:
            if a == b or b == c or a==c:     
                return True
    return False
    
def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a > 0:
        if a+ b >= c and b+ c >= a and a + c >= b:
            if a != b and b != c and a!=c:     
                return True
    return False
