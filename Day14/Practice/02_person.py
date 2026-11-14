class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_birth_year(cls,name,year):
        return cls(name,2026-year)

res= Person.from_birth_year("Amar", 24)
print(res.name, res.age)