class Employee:
    def __init__(self,salary):
        self.salary= salary
    def give_raise(self, amount):
        self.salary += amount
        print("Increase Salary:", amount)
    def show_salary(self):
        print("Current salary is: ", self.salary)

emp = Employee(25000)
emp.show_salary()
emp.give_raise(5000)
emp.show_salary()


