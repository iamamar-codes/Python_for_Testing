class Employees:
    Company= "----------GOOGLE PVT LMT--------------"

    def __init__(self, id, name):
        self.Eid=id
        self.Ename=name

    def Employee_info(self):
        print("Employee ID:", self.Eid)
        print("Employee Name:",self.Ename)

    @classmethod
    def display(cls):
        print(Employees.Company)

em1 = Employees(1,"Amar Kushwaha")
Employees.display()
em1.Employee_info()

