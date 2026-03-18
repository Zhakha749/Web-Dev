def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)

def sum_double(a, b):
    return a + b if a != b else 2 * (a + b)

def diff21(n):
    return abs(n-21) if n <= 21 else 2*abs(n-21)

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
    return abs(100-n) <= 10 or abs(200-n) <= 10

def pos_neg(a, b, negative):
    return (a < 0 and b < 0) if negative else (a*b < 0)