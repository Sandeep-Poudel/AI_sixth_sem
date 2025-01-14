import datetime
class Person():
    def __init__(self, name, age,country):
        self.county = country
        self.name = name
        self.age = age
    def determineAge(self):
        current_year = datetime.datetime.now().year
        return current_year - self.age
    
    def __str__(self):
        return (f"{self.name} is from {self.county} and is {self.determineAge()} years old.")
    
manche = Person("Sandeep",2003, "Nepal")
print(manche)
# age = manche.determineAge()
# print(age)