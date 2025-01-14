class Engine:
    def __init__(self, engineType):
        self.engineType = engineType

    def start(self):
        print(f"{self.engineType} engine started")

    def stop(self):
        print(f"{self.engineType} engine stopped")


class Wheel:
    def __init__(self, wheelType):
        self.wheelType = wheelType

    def start(self):
        print(f"{self.wheelType} wheel started")

    def stop(self):
        print(f"{self.wheelType} wheel stopped")


class Car:
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels

    def startCar(self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.start()
        print("Car started")

    def stopCar(self):
        self.engine.stop()
        for wheel in self.wheels:
            wheel.stop()
        print("Car stopped")


engine = Engine("heavy")
wheels = [Wheel("thulo") ]
car = Car(engine, wheels)
car.startCar()
car.stopCar()