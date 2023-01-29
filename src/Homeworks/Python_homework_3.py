class Person:
    def __init__(self, name, surname, age, gender, address):
        self._name = name
        self._surname = surname
        self._age = age
        self._gender = gender
        self._address = address
        
    def __repr__(self):
        return f" {self._name}, {self._surname},  {self._age}, {self._gender}, {self._address}"

class Company:
    def __init__(self, company_name, founded_at, employees_count):
        self.__company_name = company_name
        self.__founded_at = founded_at
        self.__employees_count = employees_count

    def __repr__(self):
        return f'Company(company_name={self.__company_name}, founded_at={self.__founded_at}, employees_count={self.__employees_count})'

class Job:
    def __init__(self, company, salary, experience_year, position):
        self.__company = company
        self.__salary = salary
        self.__experience_year = experience_year
        self.__position = position

    def __repr__(self):
        return f'Job(company={self.__company}, salary={self.__salary}, experience_year={self.__experience_year}, position={self.__position})'

    def change_salary(self, new_salary):
        self.__salary = new_salary

    def change_experience_year(self, new_experience_year):
        self.__experience_year = new_experience_year

    def change_position(self, new_position):
        self.__position = new_position 
    
class Date:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def __repr__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def add_day(self, days):
        self.day += days
        while self.day > self.__get_days_in_month():
            self.day -= self.__get_days_in_month()
            self.add_month(1)

    def add_month(self, months):
        if self.month == 1 and months == 1:
            self.month += months + 1
            self.day = 2
        else: self.month += months
        while self.month > 12:
            self.month -= 12
            self.add_year(1)
        
    def add_year(self, years):
        self.year += years

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self, month):
        self.__month = month

    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self, day):
        self.__day = day

    def __get_days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if self.month in [4, 6, 9, 11]:
            return 30
        if self.__is_leap_year():
            return 29
        return 28

    def __is_leap_year(self):
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
"""d = Date(2022, 1, 30)
print(d)  
d.add_month(1)
print(d)
d.add_year(2)
print(d) """
    
class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __repr__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

    def add_hour(self, hours):
        self.hour += hours
        while self.hour >= 24:
            self.hour -= 24

    def add_minute(self, minutes):
        self.minute += minutes
        while self.minute >= 60:
            self.minute -= 60
            self.add_hour(1)

    def add_second(self, seconds):
        self.second += seconds
        while self.second >= 60:
            self.second -= 60
            self.add_minute(1)

    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self, hour):
        self.__hour = hour

    @property
    def minute(self):
        return self.__minute
    @minute.setter
    def minute(self, minute):
        self.__minute = minute

    @property
    def second(self):
        return self.__second
    @second.setter
    def second(self, second):
        self.__second = second

"""t = Time(10, 30, 45)
print(t) 
t.add_hour(3)
print(t) 
t.add_minute(45)
print
"""
class DateTime:
    def __init__(self, date : Date, time: Time):
        self.__date = date
        self.__time = time

    def __repr__(self):
        return f"{self.__date} {self.__time}"
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time):
        self.__time = time

    def add_year(self, years):
        self.date.add_year(years)

    def add_month(self, months):
        self.date.add_month(months)
        if self.date.month > 12:
            self.date.month = self.date.month % 12
            self.date.add_year(1)

    def add_day(self, days):
        self.date.add_day(days)

    def add_hour(self, hours):
        self.time.add_hour(hours)
        if self.time.hour > 24:
            self.time.hour = self.time.hour % 24
            self.date.add_day(1)

    def add_minute(self, minutes):
        self.time.add_minute(minutes)
        if self.time.minute >= 60:
            self.time.minute = self.time.minute % 60
            self.add_hour(1)

    def add_second(self, seconds):
        self.time.add_second(seconds)
        if self.time.second >= 60:
            self.time.second = self.time.second % 60
            self.add_minute(1)

    def sub_year(self, year):
        self.date.year -= year
        if self.date.year < 0:
            raise Exception("Year cannot be negative.")
    
    def sub_month(self, month):
        self.date.month -= month
        while self.date.month <= 0:
            self.date.month += 12
            self.date.year -= 1
        if self.date.year < 0:
            raise Exception("Year cannot be negative.")
    
    def sub_day(self, day):
        total_days = self._days_in_month()
        self.date.day -= day
        while self.date.day <= 0:
            self.date.month -= 1
            if self.date.month == 0:
                self.date.month = 12
                self.date.year -= 1
            self.date.day += self._days_in_month()
        if self.date.year < 0:
            raise Exception("Year cannot be negative.")
    
    def sub_hour(self, hour):
        total_hours = 24
        self.time.hour -= hour
        while self.time.hour < 0:
            self.time.hour += total_hours
            self.date.day -= 1
        while self.date.day <= 0:
            self.date.month -= 1
            if self.date.month == 0:
                self.date.month = 12
                self.date.year -= 1
            self.date.day += self._days_in_month()
        if self.date.year < 0:
            raise Exception("Year cannot be negative.")
    
    def sub_minute(self, minute):
        total_minutes = 60
        self.time.minute -= minute
        while self.time.minute < 0:
            self.time.minute += total_minutes
            self.time.hour -= 1
        while self.time.hour < 0:
            self.time.hour += 24
            self.date.day -= 1
        while self.date.day <= 0:
            self.date.month -= 1
            if self.date.month == 0:
                self.date.month = 12
                self.date.year -= 1
            self.date.day += self._days_in_month()
        if self.date.year < 0:
            raise Exception("Year cannot be negative.")
    
    def sub_second(self, second):
        total_seconds = 60
        self.time.second -= second
        while self.time.second < 0:
            self.time.second += total_seconds
            self.time.minute -= 1
        while self.time.minute < 0:
            self.time.minute += 60
            self.time.hour -= 1
        while self.time.hour < 0:
            self.time.hour += 24
            self.date.day -= 1
        while self.date.day <= 0:
            self.date.month -= 1
            if self.date.month == 0:
                self.date.month = 12
                self.date.year -= 1

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time):
        self.__time = time

    def __add__(self, other):
        year = self.date.year + other.date.year
        month = self.date.month + other.date.month
        day = self.date.day + other.date.day
                
        hour = self.time.hour + other.time.hour
        minute = self.time.minute + other.time.minute
        second = self.time.second + other.time.second
        carry, second = divmod(second, 60)
        minute += carry
        carry, minute = divmod(minute, 60)
        hour = (hour + carry) % 24

        if day > 28:
            if self.date.month == 2 and self.is_leap_year():
                day = 29
            elif self.date.month in [1, 3, 5, 7, 8, 10, 12]:
                day = 31
            elif self.date.month in [4, 6, 9, 11]:
                day = 30
        
        if month > 12:
            year += month // 12
            month = month % 12
        
        return DateTime(Date(year, month, day), Time(hour, minute, second))


    def __sub__(self, other):
        
            delta1 = (self.date.year - other.date.year) * 365 + (self.date.month - other.date.month) * 30 + (self.date.day - other.date.day)
            new_date = Date(self.date.year, self.date.month, self.date.day - delta1)
            total_seconds_t1 = self.time.hour * 3600 + self.time.minute * 60 + self.time.second
            total_seconds_t2 = other.time.hour * 3600 + other.time.minute * 60 + other.time.second
            difference_in_seconds = total_seconds_t1 - total_seconds_t2
            hours, remainder = divmod(difference_in_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            new_time = Time(hours, minutes, seconds)
            
            return DateTime(new_date, new_time)
            
"""date = Date(2023, 1, 29)
time = Time(13, 30, 45)
datetime = DateTime(date, time)
print(datetime) 
datetime.add_hour(5)
print(datetime) 
datetime.add_day(2)
print(datetime) 
datetime.sub_month(3)
print(datetime)
datetime.sub_year(2)
print(datetime)
dt1 = DateTime(Date(2022, 12, 31), Time(23, 59, 59))
dt2 = DateTime(Date(0000, 0, 0), Time(0, 0, 1))
t1 = DateTime(Date(2000, 2, 3), Time(1, 20, 30))
t2 =DateTime(Date(2000, 2, 3), Time(0, 40, 20))
result =t1-t2
dt3 = dt1 + dt2
print(dt3)
print(result) """ 


class Money():
    exchange = {'AMD': 1, 'RUB': 5.8, 'USD': 400, 'EUR': 430}
    class MoneyError(Exception):
        pass

    def __init__(self, amount, currency):
        try:
            if not isinstance(amount, (int, float)):
                raise self.MoneyError("Amount should be a number.")
            if not isinstance(currency, str):
                raise self.MoneyError("Currency should be a string.")
        except Exception as e:
            print(e)

        self.__amount = amount
        self.__currency = currency
    def __repr__(self):
        return "{}:{}".format(self.__amount, self.__currency)
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount):
        self.__amount = amount
        return self.__amount
    @property
    def currency(self):
        return self.__currency
    @currency.setter
    def currency(self, currency):
        self.__currency = currency
        return self.__currency
    
    def conversation(self,target_currency):
        rate = self.exchange[target_currency] / self.exchange[self.currency]
        return Money(round(self.amount * rate, 2), target_currency)

    def __add__(self, other):
        if self.currency != other.currency:
            other = other.conversation(self.currency)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            other = other.conversation(self.currency)
        return Money(self.amount - other.amount, self.currency)

    def __truediv__(self, other):
        if self.currency != other.currency:
            other = other.conversation(self.currency)
        return Money(self.amount / other.amount, self.currency)

    def __eq__(self, other):
        if self.currency != other.currency:
            other = other.conversation(self.currency)
        return self.amount == other.amount

    def __ne__(self, other):
        if self.currency != other.currency:
            other = other.conversation(self.currency)
        return self.amount != other.amount

    def __lt__(self, other):
        if self.currency != other.currency:
            other = other.conversation(self.currency)
        return self.amount < other.amount

    def __gt__(self, other):
        if self.currency != other.currency:
            other = other.conversation(self.currency)
        return self.amount > other.amount

    def __le__(self, other):
        if self.currency != other.currency:
            other = other.conversation(self.currency)
        return self.amount <= other.amount

    def __ge__(self, other):
        if self.currency != other.currency:
            other = other.conversation(self.currency)
        return self.amount >= other.amount
    
"""money1 = Money(100, 'USD')
print(money1)
money2 = Money(200, 'EUR')
print(money2)
money1_in_rub = money1.conversation('RUB')
print(money1_in_rub)
result = money1 + money2
print(result)
result = money2 - money1
print(result)
result = money1 / money2
print(result)"""

class MyRange:
    class MyRangeError(Exception):
        pass

    def __init__(self, current, end, step=1):
        try:
            if current >= end:
                raise self.MyRangeError("Current value should be less than end value.")
        except Exception as e:
            print(e)
    
        self.__current = current
        self.__end = end
        self.__step = step

    def __repr__(self):
        return f'MyRange({self.__current}, {self.__end}, {self.__step})'

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current >= self.__end:
            raise StopIteration
        else:
            current = self.__current
            self.__current += self.__step
            return current

    def __len__(self):
        return (self.__end - self.__current) // self.__step + 1

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        return self.__current + index * self.__step

    def __reversed__(self):
        current = self.__end - 1 if self.__end > self.__current else self.__end + 1
        while current != self.__current:
            yield current
            current -= self.__step


#my_range = MyRange(10, 20, 2)
#iter_obj = iter(my_range)
#print(next(iter_obj)) 
#print(next(iter_obj)) 
#print(len(my_range))
#print(my_range[2]) 
#reversed_range = reversed(my_range)
#print(list(reversed_range))

class Doctor(Person):
    class DoctorError(Exception):
        pass

    def __init__(self, name, surname, age, gender, address, department, profession, patronymic, salary:Money):
        try:
            if not all(map(lambda x: isinstance(x, str), (name, surname, gender, address, department, profession, patronymic))):
                raise self.DoctorError("Name, surname, gender, address, department, profession, patronymic should be strings.")
        except Exception as e:
            print(e)
        super().__init__(name, surname, age, gender, address)
        self.__department = department
        self.__profession = profession
        self.__patronymic = patronymic
        self.__salary = salary

    def __repr__(self):
        return f"Doctor({self._name} {self._surname}, {self.__department}, {self.__profession})"
    @property
    def department(self):
        return self.__department
    
    @department.setter
    def department(self, department):
        self.__department = department

    @property
    def profession(self):
        return self.__profession
    
    @profession.setter
    def set_profession(self, profession):
        self.__profession = profession
  
    @property
    def patronymic(self):
        return self.__patronymic
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def set_salary(self, salary):
        self.__salary = salary

"""drJohn = Doctor("John", "Doe", 30, "Male", "123 Main St.", "Cardiology", "MD", "Smith", money1)
drJane = Doctor("Jane", "Doe", 25, "Female", "456 Main St.", "Neurology", "MD", "Johnson", money1)
print(drJohn.department)
drJohn.department = "Oncology"
print(drJohn.department) 
print(drJane.salary)
print(drJane.profession)
drJane.__profession = "PhD"
print(drJane.profession)
print(drJohn.patronymic) """


class City:
    class CityError(Exception):
        pass

    def __init__(self, name : str, mayor : Person, population : int, language : str):
        try:
            if not all(map(lambda x: isinstance(x, str), (name,  language ))):
                raise self.CityError("Name,language should be strings.")
        except Exception as e:
            print(e)

        self.__name = name
        self.__mayor = mayor
        self.__population = population
        self.__language = language

    def __repr__(self):
        return f'City({self.__name}, {self.__mayor}, {self.__population}, {self.__language})'
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def mayor(self):
        return self.__mayor
    
    @mayor.setter
    def mayor(self, mayor):
        self.__mayor = mayor

    @property
    def population(self):
        return self.__population
    
    @population.setter
    def population(self, population):
        self.__population = population

    @property
    def language(self):
        return self.__language
    
    @language.setter
    def language(self, language):
        self.__language = language

"""p = Person("Mike", "Bloomberg", "male", 56, "new york")
new_city = City('New York', p, 8175133, 'English')
print(new_city.name) 
new_city.name = 'New York City'
print(new_city.name) 
print(new_city.mayor._name) 
new_city.mayor = 'Bill de Blasio'
print(new_city.mayor) 
print(new_city.population)
new_city.population = 8598748
print(new_city.population)
print(new_city.language) 
new_city.language = 'English and Spanish'
print(new_city.language) """


class University():
    class UniversityError(Exception):
        pass
    def __init__(self, name:str, founded_at:Date, rector:Person, city):
        try:
            if not all(map(lambda x: isinstance(x, str), (name ))):
                raise self.UniversityError("Name should be strings.")

        except Exception as e:
            print(e)
    
        self.__name = name
        self.__founded_at = founded_at
        self.__rector = rector
        self.__city = city

    def __repr__(self):
        return "{}, {}, {}, {}". format(self.__name, self.__founded_at, self.__rector, self.__founded_at)
    @property
    def name(self):
        return self.__name
    @name.setter
    def set_name(self, name):
        self.__name = name
        return self.__name
    @property
    def founded_at(self):
        return self.__founded_at
    @founded_at.setter
    def set_rector(self, rector):
        self.__rector = rector
        return self.__rector
    @property
    def rector(self):
        return self.__rector
    @property
    def city(self):
        return self.__city
    
"""rector = Person("John", "Doe","male", 35, "New york")
city = City("New York", Person("Mike", "Bloomberg", "male",56, "New York"), 8000000, "English")
university1 = University("NYU", Date(1831,4,18), rector, city)
print(university1)
print(university1.founded_at)
print(university1.name)"""


class Teacher(Person):
    class TeacherError(Exception):
        pass

    def __init__(self, name, surname, age, gender, address, university : University, faculty : str, experience : int, start_work_at : Date, subject : int, salary : Money):
        try:
            if not all(map(lambda x: isinstance(x, str), (name, surname,  gender, address, faculty, subject))):
                raise self.TeacherError("name, surname,  gender, address, faculty, subject should be strings.")
        except Exception as e:
            print(e)
        super().__init__(name, surname, age, gender, address)
        self.__university = university
        self.__faculty = faculty
        self.__experience = experience
        self.__start_work_at = start_work_at
        self.__subject = subject
        self.__salary = salary

    def __repr__(self):
        return f"{self._name}, {self._surname}, {self._age}, {self._gender}, {self._address}, {self.__university}, {self.__faculty}, {self.__experience}, {self.__start_work_at}, {self.__subject}, {self.__salary}"
    @property
    def university(self):
        return self.__university
    @university.setter
    def university(self, university):
        self.__university = university
    @property
    def faculty(self):
        return self.__faculty
    @faculty.setter
    def faculty(self, faculty):
        self.__faculty = faculty
    @property
    def experience(self):
        return self.__experience
    @experience.setter
    def set_experience(self, experience):
        self.__experience = experience
    @property
    def start_work_at(self):
        return self.__start_work_at
    @start_work_at.setter
    def set_start_work_at(self, start_work_at):
        self.__start_work_at = start_work_at
    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject):
        self.__subject = subject
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary

"""teacherJohn = Teacher("John", "Doe", 45, "Male", "789 Main St.", university1, "Mathematics", 20, Date(2000, 1, 1), "Algebra", money1)
teacherJane = Teacher("Jane", "Doe", 40, "Female", "999 Main St.",university1, "History", 15, Date(2005, 1, 1), "European History",money2)
print(teacherJane.salary)
print(teacherJohn)"""


class Student(Person):
    class StudentError(Exception):
        pass

    def __init__(self, name, surname, age, gender, address, university : University, faculty : str, course : int, started_at : Date):
        try:
            if not all(map(lambda x: isinstance(x, str), (name, surname, gender, address, faculty))):
                raise self.StudentError("Name, surname, gender, address, university, faculty should be strings.")
        except Exception as e:
            print(e)

    
        super().__init__(name, surname, age, gender, address)
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__started_at = started_at

    def __repr__ (self):
        return f"{self._name}, {self._surname}, {self._age}, {self._gender}, {self._address}, univerity: {self.__university}, {self.__faculty}, {self.__course}, {self.__started_at}"
    @property
    def university(self):
        return self.__university
    @university.setter
    def university(self, university):
        self.__university = university
    @property
    def faculty(self):
        return self.__faculty
    @faculty.setter
    def faculty(self, faculty):
        self.__faculty = faculty
    @property
    def course(self):
        return self.__course
    @course.setter
    def set_course(self, course):
        self.__course = course
    @property
    def started_at(self):
        return self.__started_at
    @started_at.setter
    def set_started_at(self, started_at):
        self.__started_at = started_at

"""studentJohn = Student("John", "Doe", 20, "Male", "789 Main St.", university1, "Computer Science", 3, Date(2020, 1, 1))
studentJane = Student("Jane", "Doe", 18, "Female", "999 Main St.", university1, "Business", 1, Date(2022, 1, 1))
print(studentJohn.university)
print(studentJane)
studentJane.faculty = "Data science"
print(studentJane.faculty)"""

#Create a decorator that counts the number of times a function has been called.
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f"{func.__name__} has been called {wrapper.count} times.")
        return result

    wrapper.count = 0
    return wrapper

@count_calls
def my_func():
    pass
my_func() 
my_func()