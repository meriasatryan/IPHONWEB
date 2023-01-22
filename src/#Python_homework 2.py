"""#Task 1
def my_dict(dict):
    keys_to_delete = ["age", "city"]
    for key in keys_to_delete:
        dict.pop(key)
    return dict 

print(my_dict({"name":"Kelly", "age" : 25, "salary":8000, "city":"New York"})) 


#Task 2

def min_value(dict):
    min_value = sorted(dict.values())[0]
    return list(dict.keys())[list(dict.values()).index(min_value)]

print(min_value({"Physics":82, "Math" : 65, "History" : 75}))

#Task 3

def copy_content(my_text, empty):
    with open(str(my_text) + ".txt", "r") as file1:
        lines = file1.readlines()
        with open(str(empty) + ".txt", "w") as file2:
            for i in range(len(lines)):
                file2.write(lines[i])
copy_content("my_text", "empty")


#Task 4 

import string
def frequency(my_text):
    dict = {}
    with open(str(my_text) + ".txt", "r") as file:
        lines = file.readlines()
        lines = str(lines).lower()
        words = lines.split(" ")

        for word in words:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word]=1
        return dict
print(frequency("my_text"))

#Task 5 

def read_last_n(my_text ,n):
    with open(str(my_text) + ".txt", "r") as file:
        lines = file.readlines()
        for i in range(len(lines)-n,len(lines)):
            return lines[i]
        
print(read_last_n("my_text",2))

#Task 6

class Company:
    def __init__(self, company_name, founded_at, employees_count):
        self.company_name = company_name
        self.founded_at = founded_at
        self.employees_count = employees_count

    def __repr__(self):
        return f'Company(company_name={self.company_name}, founded_at={self.founded_at}, employees_count={self.employees_count})'

class Job:
    def __init__(self, company, salary, experience_year, position):
        self.company = company
        self.salary = salary
        self.experience_year = experience_year
        self.position = position

    def __repr__(self):
        return f'Job(company={self.company}, salary={self.salary}, experience_year={self.experience_year}, position={self.position})'

    def change_salary(self, new_salary):
        self.salary = new_salary

    def change_experience_year(self, new_experience_year):
        self.experience_year = new_experience_year

    def change_position(self, new_position):
        self.position = new_position

class Person:
    def __init__(self, name, surname, gender, age, address):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.address = address
        self.friends = []
        self.jobs = []

    def __repr__(self):
        return f'Person(name={self.name}, surname={self.surname}, gender={self.gender}, age={self.age}, address={self.address}, friends={self.friends}, jobs={self.jobs})'

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        self.friends.remove(friend)

    def add_job(self, job):
        self.jobs.append(job)
        job.company.employees_count += 1

    def remove_job(self, job):
        self.jobs.remove(job)
        job.company.employees_count -= 1

    def display_jobs(self):
        for job in self.jobs:
            print(job)

company1 = Company('ABC', '1998', 10)

job1 = Job(company1, 50000, 2, 'Engineer')
job2 = Job(company1, 60000, 3, 'Data Scientist')

person1 = Person('Mery', 'Asatryan', 'Female', 19, 'Yerevan')
person2 = Person('Jane', 'Doe', 'Female', 25, '456 Park Ave')

person1.add_friend(person2)

person1.add_job(job1)
person2.add_job(job2)

print('Jobs of Person 1:')
person1.display_jobs()
print('Jobs of Person 2:')
person2.display_jobs()

print(f'Employees count in {company1.company_name}: {company1.employees_count}')

"""
#Task 7

class Date():
    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        if self.day < 10:
            if self.month <10:
                return f'0{self.day}.0{self.month}.{self.year}'
            else: return f'0{self.day}.{self.month}.{self.year}'

        elif self.month < 10:
            if self.day > 10:
                return f'{self.day}.0{self.month}.{self.year}'
        else:
            return f'{self.day}.{self.month}.{self.year}'
        
    
    def add_day(self, days):
        self.day += days
        while self.day > self.__days_in_month():
            self.day -= self.__days_in_month()
            self.add_month(1)

    def add_month(self, months):
        self.month += months
        while self.month > 12:
            self.month -= 12
            self.year += 1

    def add_year(self, years):
        self.year += years

    def __days_in_month(self):
        if self.month in (4, 6, 9, 11):
            return 30
        elif self.month == 2:
            return 29 if self.__is_leap_year() else 28
        else:
            return 31
        
    def __is_leap_year(self):
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            return self.year, "is leap"
        return self.year, "is NOT leap"
    

date1 = Date(15, 10, 1960)
print(date1)
date1.add_day(30)
print(date1)
date1.add_month(3)
print(date1)
date1.add_year(25)
print(date1)

class Time():
    def __init__(self, hour:int, minute:int, second:int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return f'{self.hour}:{self.minute}:{self.second}'

    def add_second(self, seconds):
        self.second += seconds
        self.__normalize()
    
    def add_minute(self, minutes):
        self.minute += minutes
        self.__normalize()

    def add_hour(self, hours):
        self.hour += hours
        self.__normalize()

    def __normalize(self):
        self.minute += self.second // 60
        self.second %= 60
        self.hour += self.minute // 60
        self.minute %= 60
        self.hour %= 24


    def __add__(self, other):
        new_time = Time(self.hour, self.minute, self.second)
        new_time.add_second(other.second)
        new_time.add_minute(other.minute)
        new_time.add_hour(other.hour)
        return new_time 
  

def sum(time1, time2):
    hour = time1.hour + time2.hour
    minute = time1.minute + time2.minute
    second = time1.second + time2.second
    hour += minute // 60
    minute %= 60
    hour %= 24
    return Time(hour, minute, second)     
   
time1 = Time(12, 30, 45)
time2 = Time(1, 15, 30)
print(time1)
print(time2)
time1.add_second(35)
print(time1) 
time1.add_minute(10)
print(time1) 
time1.add_hour(2)
print(time1) 
sum = sum(time1,time2)
print(sum)

#Correct this!!!!!
date1 = Date(2000, 1, 31)
print(date1)
date1.add_month(1)
print(date1)