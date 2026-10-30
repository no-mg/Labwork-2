#родитель
class Coffee: 
    strength = 0

    def drink(self):
        print(f"Кофе, крепостью {self.strength}")

#дочки
class Espresso(Coffee):
    strength = 9

class Cappuccino(Coffee):
    strength = 5

class TurkishCoffee(Coffee):
    strength = 8

#класс знает как варить кофе, но какой вид нет
class CoffeeMachine:
    def make_coffee(self): #фабричный метод
        pass # не знает какой кофе делать
    
    def serve(self):
        coffee = self.make_coffee()
        coffee.drink()

# конкретные кофе варим
class EspressoMachine(CoffeeMachine):
    def make_coffee(self):
        return Espresso()


class CappuccinoMachine(CoffeeMachine):
    def make_coffee(self):
        return Cappuccino()


class TurkishCoffeeMachine(CoffeeMachine):
    def make_coffee(self):
        return TurkishCoffee()

machine = EspressoMachine()
machine.serve()

machine = CappuccinoMachine()
machine.serve()