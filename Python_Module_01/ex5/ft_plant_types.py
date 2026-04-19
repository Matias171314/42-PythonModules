class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._days_age = 0
        self.set_height(height)
        self.set_age(days_age)

    def show(self) -> None:
        print(f"{self._name} : {self._height}cm, {self._days_age} days old")

    def grow(self, growth_rate: float = 2.1) -> None:
        self._height = round(self._height + growth_rate, 1)

    def age(self) -> None:
        self._days_age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days_age = new_age


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days_age: int, color: str) -> None:
        super().__init__(name, height, days_age)
        self.color = color
        self.is_blooming = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self.is_blooming = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days_age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days_age)
        self.trunk_diameter = trunk_diameter
        self.shader = False

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.shader = True
        print(f"Tree {self._name} now produce a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days_age: int, harvest_season: str) -> None:
        super().__init__(name, height, days_age)
        self.harvest_season = harvest_season.capitalize()
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        super().age()

    def grow(self, growth_rate: float = 2.1) -> None:
        super().grow(growth_rate)
        self.nutritional_value += 1

    def grow_and_age(self, age_for: int) -> None:
        for i in range(age_for):
            self.grow()
            self.age()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    print("[asking the rose to bloom]")
    rose.show()
    print("")

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("")

    print("=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, "april")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow_and_age(20)
    tomato.show()
