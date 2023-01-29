#Task1
#ax**2+b*x+c=0
def abc(a,b,c):
    D = b **2-4*a*c
    if D < 0:
        print (" This equation does not have a solution")
    x1 = -b + D ** 0.5
    x2 = -b - D ** 0.5
    if D == 0:
        print("This equation has only this solution:", x1)
        return x1
    #print("The solutions are:", x1, x2)
    return x1, x2

abc(1, -6, 8)
abc(1, 5, 6)
abc(2, 0, -9)

#Task2 

def triangle(a,b):
    c = (a**2 + b**2)**0.5
    return c

print(triangle(3, 4))


#Task3
def last_digit_math(n: int):
    if n >= 0:
        last = n % 10
        return last
    return "Your number is not natural"

print(last_digit_math(56))


def last_digit_string(n: str):
    n = str(n)
    last = n[-1]
    return last

print(last_digit_string(59))

#Task4

def sum_and_product_string(n:int):
    n = str(n)
    sum = 0
    product = 1
    for i in range(len(n)):
        sum = sum + int(n[i])
        product = product*int(n[i])
        i = i + 1
    return sum, product

print(sum_and_product_string(75))


def sum_and_product_math(n: int):
    sum = 0
    product = 1
    while n!=0:
        sum += n%10
        product = product*(n%10)
        n=n//10
    return sum, product

print(sum_and_product_math(75))


#Task5

def distance(x1,y1, x2, y2):
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return distance

print(distance(3, 5, 6, 7))


#Task6
def string(string: str, n: int):
    new_string = string [:n] + string [n+1:]
    return new_string
print(string("Hello world", 7))


#Task7
def new_string(string: str):
    new_string = string[-1] + string[1:-1] + string[0]
    return new_string

print(new_string("hello"))

#Task8
def round_float(n:float):
    res = (n - n // 1) * (10 ** 3) // 1
    if res % 10 < 5:
        return n // 1 + res // 10 * (10 ** -2)
    else:
        return n // 1 + (res // 10 + 1) * (10 ** -2)


print(round_float(4.34537573254))
print(round_float(5.375763))


#Task9
def min_max(a, b, c):
    if a>b and a>c:
        max = a
    elif b > c:
        max = b
    else:
        max = c
    if a<b and a<c:
        min = a
    elif b < c:
        min = b
    else:
        min = c
    return min, max
    
print(min_max(5, 33, 8))



#Task10
def odd_even(n):
    if n%2==0:
        return "This number is even"
    return "This number is odd"

print(odd_even(4))


#Task11
def divides(n):
    if n%5 == 0 and n%7 == 0:
        return True
    return False
print(divides(35))


#Task12
def string_index_divides(string:str):
    sum = ""
    for i in range(len(string)):
        if i%3 == 0:
            sum += string[i]
    return sum
print(string_index_divides("hello world"))


def string_index_divides_slicing(string:str):
    sum = string[::3]
    return sum
print(string_index_divides_slicing("hello world"))



#Task13
def divisors(n):
    divisors = []
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
        i+=1
    return divisors
print(divisors(36))

#Task14
def matrix(n,m):
    matrix = ""
    for i in range(n):
        matrix=(" * " * m)
        print(matrix)
        i+=1

matrix(4, 8)

#Task15
def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return factorial

print(factorial(4))


#Task16
def gcd(a, b):
    gcd = 0
    for i in range(1,b+1):
        if a%i == 0 and b%i==0:
            gcd = i
    return gcd

print(gcd(35, 63))


#Task17
??????
def sum(n: int):
    summ = 0
    count = 0
    while n!=0:
        summ += n%10
        n=n//10
        print(summ)
        if summ%10!=0:
            sum(summ)

        
sum(159)

        


            








    


