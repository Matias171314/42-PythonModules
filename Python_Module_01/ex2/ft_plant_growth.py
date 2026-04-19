class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days_age = days_age

    def show(self) -> None:
        print(f"{self.name} : {self.height}cm, {self.days_age} days old")

    def grow(self, growth_rate: float = 0.8) -> None:
        self.height = round(self.height + growth_rate, 1)

    def age(self) -> None:
        self.days_age += 1


if __name__ == "__main__":
    rose = Plant("rose", 25.0, 30)
    start_heigh = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()
    for days in range(1, 8):
        print(f"=== Day {days} ===")
        rose.grow()
        rose.age()
        rose.show()
    total_growth = round(rose.height - start_heigh, 1)
    print(f"Growth this week: {total_growth}cm")
