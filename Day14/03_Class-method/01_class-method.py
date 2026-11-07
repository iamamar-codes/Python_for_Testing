class Employees:
    Company= "----------GOOGLE PVT LMT--------------"

    def __init__(self, id, name,job):
        self.Eid=id
        self.Ename=name
        self.Ejob=job

    def Employee_info(self):
        print("Employee ID:", self.Eid)
        print("Employee Name:",self.Ename)
        print("Employee Job:",self.Ejob)

    @classmethod
    def display(clg):
        print(Employees.Company)

em1 = Employees(1,"Amar Kushwaha","SDET")
em2 = Employees(2,"Raman Singh", "SD")
em3= Employees(3,"Rohan Kumar","DA")
Employees.display()
em1.Employee_info()
em2.Employee_info()
em3.Employee_info()
