text: str = "value"
num: int = 10
temp: float = 37.5


class city:
    def __init__(self, name, location):
        self.name = name 
        self.location = location

number:int | float = 12
optional: str | None

digits: list[int] = [1, 2, 3, 4, 5]

table_5: tuple[int, ...] = (1, 2, 3, 4, 5)

hampsire = city("Hamsire", 4568932)
temp_city: tuple[city, float] = (hampsire, 20.5)


def root(num: int, exp: float | None = .5) -> float:
    return pow(num, .5)

print(root(25))