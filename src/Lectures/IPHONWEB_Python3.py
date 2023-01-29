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