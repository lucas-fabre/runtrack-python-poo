class Operation:
    def __init__(self):
        self.nombre1 = 7
        self.nombre2 = 10

    def addition(self):
        self.result = self.nombre1 + self.nombre2
        print(self.result)

Addition = Operation()
Addition.addition()