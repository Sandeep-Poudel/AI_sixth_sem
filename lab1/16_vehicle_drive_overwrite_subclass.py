class Vehicle():
    def __init__(self,make , model):
        self.make = make
        self.model = model
        
    def drive(self):
        print(f"Driving the {self.make} {self.model}.")

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def drive(self):
        print(f"Driving the {self.make} {self.model} Car.")


Gadi = Vehicle("Mahindra", "Thar")
Gadi.drive()
sanoGadi = Car("Maruti", "SuZuki")
sanoGadi.drive()