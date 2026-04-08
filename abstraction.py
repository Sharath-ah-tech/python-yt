class Salary:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def show(self):
        print(f"{self.name}\nYour Salary is {self.final_amount()}\nYour role is {self.position()}\n")
    def calculate_tax(self):
        if self.__salary <= 50000:
            tax = self.__salary * 0.1
        elif self.__salary <= 100000:
            tax = self.__salary * 0.2
        else:
            tax = self.__salary * 0.3
        return tax
    def final_amount(self):
        return self.__salary-self.calculate_tax()
    def position(self):
        if self.__salary <= 50000:
            return "Junior"
        elif self.__salary <= 100000:
            return "Mid-level"
        else:
            return "Senior"
s1=Salary("Shardhur", 50000)
s2=Salary("Satyarth", 75000)
s3=Salary("Sahil", 150000)

s1.show()
s2.show()
s3.show()