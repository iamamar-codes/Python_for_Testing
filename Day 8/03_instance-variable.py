class employee:
    # class variable
    company = "TCS"
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def info(self):
        # Instance variable
        print("Employee Id is:", self.id)
        print("Employee name is:",self.name)
        print("Company:",employee.company)

em1  = employee(212, "Ramesh")
# print(employee.company)
em1.info()

em2 = employee(202, "Suresh")
em1.info()