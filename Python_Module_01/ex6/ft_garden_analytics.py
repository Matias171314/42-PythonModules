class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
            self.shade_calls = 0

    def __init__(self, name: str, height: float, days_age: int) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._days_age = 0
        self.set_height(height)
        self.set_age(days_age)
        self._growth_rate = 0.8
        self._analytics = self._Stats()

    def show(self) -> None:
        print(f"{self._name} : {self._height}cm, {self._days_age} days old")
        self._analytics.show_calls += 1

    def grow(self, days: int = 1) -> None:
        self._height = round(self._height + (self._growth_rate * days), 1)
        self._analytics.grow_calls += 1

    def age(self, days: int = 1) -> None:
        self._days_age += days
        self._analytics.age_calls_calls += 1

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

    @staticmethod
    def is_older_1y(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


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
        self._analytics.shade_calls += 1


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days_age: int, harvest_season: str) -> None:
        super().__init__(name, height, days_age)
        self.harvest_season = harvest_season.capitalize()
        self.nutritional_value = 0
        self._growth_rate = 2.1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        super().age()

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 days_age: int, color:  str) -> None:
        super().__init__(name, height, days_age, color)
        self.count_seed = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.count_seed}")

    def bloom(self) -> None:
        super().bloom()
        self.count_seed = 42


def display_statistics(plant: Plant) -> None:
    stats = plant._analytics
    print(f"Stats: {stats.grow_calls} grow, {stats.age_calls} age, "
          f"{stats.show_calls} show")
    if isinstance(plant, Tree):
        print(f"{stats.shade_calls} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_1y(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_1y(400)}")
    print("")

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)
    print("")

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_statistics(oak)
    print("")

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)
    print("")

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_statistics(anonymous)
