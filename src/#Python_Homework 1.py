#Homework 1 
#Task 1
def progression(first, second, n):
    nth = first + (n-1)*(second - first)
    return nth

print (progression(1, 2, 4))

#Task 2
def ratiorg(list):
    sum = 0
    list = list.split(" ")
    for item in list:
        if item.isnumeric():
            sum += int(item)
    return sum

print(ratiorg("2 apples, 12 finds"))

#Task3

def is_sorted(numbers):
    if (numbers[0] <= numbers[1] <= numbers[2]) or (numbers[0] >= numbers[1] >= numbers[2]):
        return "Sorted"
    else:
        return "Unsorted"

print(is_sorted([1,2,3]))
print(is_sorted([7,5,1]))
print(is_sorted([2,7,3]))

#Task4

def perfect_number(n):
    sum = 0
    for num in range(1,n):
        if n%num == 0:
            sum += num
            print(sum) 
            num+=1
        elif sum == n:
            return "This number is perfect"
        else: 
            return "This number is NOT perfect"
 
print(perfect_number(6))
print(perfect_number(12))

#Task5

def sum(list):
    sum = 0
    for i in range(len(list)):
        sum+=list[i]
        i+=1
    return sum
print(sum([1,2,3,4]))



#Task6

def maximum(list):
    max = list[0]
    for element in list:
        if element > max:
            max = element
    return max
   
print(maximum([1,2,3,4]))

#Task7

def removing(list, element):
    while element in list:
        list.remove(element)
    print(list)

removing([1,2,3,4,4,4,4,5], 4)

#Task8

def product(list):
    product = 1
    for i in range(len(list)):
        product*=list[i]
        i+=1
    return product
print(product([1,2,3,4]))


#Task9

def inverse(string):
    if len(string)%4==0:
        return string[::-1]
    else:
        return string

print(inverse("hello world!"))

#Task10

def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
print(fibonacci_iterative(6))


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(6))


#Task11

def lcm(a,b):
    gcd = 0
    for i in range(1,b+1):
        if a%i == 0 and b%i==0:
            gcd = i
            lcm = a*b /gcd
    return lcm

print(lcm(6,12))


#Task12

def next_palindrome(n):
    n+=1 
    while str(n)!=str(n)[::-1]:
        n+=1
    return n

print(next_palindrome(119))

#Task13

def robot(x,y,commands):
    for item in commands:
        if item == "left":
            x-=1
        elif item == "right":
            x+=1
        elif item == "up":
            y+=1
        elif item == "down":
            y-=1
    
    return x, y

print(robot(0,0, ["down", "left", "up", "down", "right", "right"]))


#Task 14
def one_step_cyclic(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i:] + list1[:i] == list2:
                return True
        return False

print(one_step_cyclic([1,2,3,4,5,6],[6,1,2,3,4,5]))

#Task15
def delete_digit(n):
    n = str(n)
    all_possible = []
    for i in range(len(n)):
        num = int(n[:i] + n[i+1:])
        all_possible.append(num)
    return max(all_possible)
print(delete_digit(152))  
print(delete_digit(1001)) 

#Task16
def mytuple(tuple):
    numbers=[]
    for i in tuple:
        if str(i).isnumeric():
            numbers.append(i)
    return numbers

print(mytuple((1,5,"hello", 4, 100,"world")))


#Task17
def add_tuple(tuple, object):
    new = tuple + (object,)
    return new
print(add_tuple(("hello", 4, 5), "world"))


#Task18
def tuple_into_string(tuple):
    string = " "
    for item in tuple:
        string = string + str(item) + "`-´" 
    return string
print(tuple_into_string((1,2,3,"hello", "hi", "nice to meet you")))

#Task19
def length(list):
    length=0
    for i in list:
        length += 1
    return length
print(length([1,2,3,4,5,6,7,8]))

#Task20
def lucky_ticket(number):
    left = 0
    right = 0
#I didn´t use string method, I just used str() function to find the length of my number, there is no other way
    for i in range(int(len(str(number))/2)+1):
        left+=(number%(10**i))/(10**(i-1))
        number-=number%(10**i)
        i+=1

    for i in range(int(len(str(number))/2)+1, int(len(str(number)))+1 ):
        right+=(number%(10**i))/(10**(i-1))
        number-=number%(10**i)
        i+=1

    if right == left:
        return True
    else:
        return False

print(lucky_ticket(123456))
print(lucky_ticket(1230))
print(lucky_ticket(239017))
        
#Task21

def euler_function(n):
    count = 0
    for i in range(1, n+1):
        if gcd(i, n) == 1:
            count += 1
    return count

def gcd(a, b):
    gcd = 0
    for i in range(1,b+1):
        if a%i == 0 and b%i==0:
            gcd = i
    return gcd

print(euler_function(6))
print(euler_function(10))


#Task 22*
def remove_anagrams(words):
    i = 1
    while i < len(words):
        if sorted(words[i-1]) == sorted(words[i]):
            del words[i]
        else:
            i += 1
    return words
print(remove_anagrams(["abba","baba","bbaa","cd","cd"]))

#Task23**

def sort_by_height(names, heights):

    combined = zip(names, heights)
    sorted_people = sorted(combined, key=lambda x: x[1], reverse=True)
    sorted_names = [person[0] for person in sorted_people]
    return sorted_names

print(sort_by_height( ["Mary","John","Emma"],[180,165,170]))
print(sort_by_height( ["Alice","Bob","Bob"],[155,185,150]))




