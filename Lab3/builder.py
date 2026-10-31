#что собираем
class LegoSet:
    def __init__(self):
        self.name = ""
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def __str__(self):
        parts_str = ", ".join(self.parts)
        return f"{self.name}: {parts_str}"


#родитель общие шаги 
class LegoBuilder:
    def __init__(self, tail_flag=False, wings_flag=False):
        self.set = LegoSet()
        self.has_tail = tail_flag
        self.has_wings = wings_flag

    def build_head(self):
        pass

    def build_body(self):
        pass

    def build_tail(self):
        pass

    def build_wings(self):
        pass

    def build_details(self):
        pass

    def get_result(self):
        return self.set


# дети, конкретно что собираем
class SquirrelBuilder(LegoBuilder):
    def __init__(self, tail_flag=True, wings_flag=False):
        super().__init__(tail_flag, wings_flag)

    def build_head(self):
        self.set.name = "Белка"
        self.set.add("Маленькие рыжие детали 7шт, черные 2шт")

    def build_body(self):
        self.set.add("Большие рыжие детали 8 шт")

    def build_tail(self):
        self.set.add("Маленькие рыжие детали 5шт")

    def build_details(self):
        self.set.add("Желтый круг")


class FoxBuilder(LegoBuilder):
    def __init__(self, tail_flag=True, wings_flag=False):
        super().__init__(tail_flag, wings_flag)

    def build_head(self):
        self.set.name = "Лиса"
        self.set.add("Маленькие рыжие детали 4шт, черные 2шт, белые 1шт")

    def build_body(self):
        self.set.add("Большие рыжие детали 8 шт, черные 4 шт")

    def build_tail(self):
        self.set.add("Маленькие рыжие детали 5шт, белые 1шт")

    def build_details(self):
        self.set.add("Рыжие треугольники 2шт")


class OwlBuilder(LegoBuilder):
    def __init__(self, tail_flag=False, wings_flag=True):
        super().__init__(tail_flag, wings_flag)

    def build_head(self):
        self.set.name = "Сова"
        self.set.add("Маленькие коричневые детали 4шт, маленькие рыжие 2шт")

    def build_body(self):
        self.set.add("Большие черные детали 5 шт")

    def build_wings(self):
        self.set.add("Серые пластины 2шт")

    def build_details(self):
        self.set.add("Желтый круг")  #клюв

#билдер то как мы собираем, в какой последовательности
class Instruction:
    def __init__(self, builder):
        self.builder = builder

    def build(self):
        self.builder.build_head()
        self.builder.build_body()
        if self.builder.has_tail:
            self.builder.build_tail()
        if self.builder.has_wings:
            self.builder.build_wings()
        self.builder.build_details()



builder = SquirrelBuilder()
Instruction(builder).build()
print(builder.get_result())