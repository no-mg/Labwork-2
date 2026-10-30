class Cat: # один кот в доме
    _instance = None

    def __new__(cls, name="Кошак"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.is_hungry = True
        return cls._instance

    def feed(self):
        self.is_hungry = False
        print(f"{self.name} уже покормлен и сыт")

# не важно сколько раз будем создавать нового кота, у нас будет возвращаться только самый первый тк условие

cat1 = Cat()
print(cat1.is_hungry)

cat1.feed()

cat2 = Cat("Пушинка")
print(cat2.name)
print(cat2.is_hungry)