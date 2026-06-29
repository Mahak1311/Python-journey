#Abstract class
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def calculate_salary(self):
        print("Rs. 28000 per month")


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Rs. 82000 per month")


class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Rs. 60000 per month")


i = Intern()
i.calculate_salary()

f = FullTimeEmployee()
f.calculate_salary()

c = ContractEmployee()
c.calculate_salary()