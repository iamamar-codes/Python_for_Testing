class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_birth_year(cls,name, birth_year):
        age =2026 - birth_year
        return cls(name,age)
    def show(self):
        print(self.name, self.age )


p1=person.from_birth_year("Amar", 2002)
p2=person("Samar", 22)
p1.show()
p2.show()