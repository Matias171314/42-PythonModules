class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow_calls(self) -> None:
            self._grow_calls += 1

        def increment_age_calls(self) -> None:
            self._age_calls += 1

        def increment_show_calls(self) -> None:
            self._show_calls += 1

        def get_grow_calls_count(self) -> int:
            return self._grow_calls

        def get_age_calls_count(self) -> int:
            return self._age_calls

        def get_show_calls_count(self) -> int:
            return self._show_calls

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float, days_age: int) -> None:
        self._name = name.capitalize()
        self._height = 0.0
        self._days_age = 0
        self.set_height(height)
        self.set_age(days_age)
        self.analytics = self.Stats()

    def show(self) -> None:
        print(f"{self._name} : {self._height}cm, {self._days_age} days old")
        self.analytics.increment_show_calls()

    def grow(self, growth_rate: float = 8.0) -> None:
        self._height = round(self._height + growth_rate, 1)
        self.analytics.increment_grow_calls()

    def age(self, age_rate: int = 1) -> None:
        self._days_age += age_rate
        self.analytics.increment_age_calls()

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
    def older_than_a_year(days: int) -> bool:
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
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        self.is_blooming = True


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def increment_shade_calls(self) -> None:
            self._shade_calls += 1

        def get_shade_calls_count(self) -> int:
            return self._shade_calls

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(self, name: str, height: float,
                 days_age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days_age)
        self.trunk_diameter = trunk_diameter
        self.shader = False
        self._tree_stats = self.TreeStats()
        self.analytics = self._tree_stats

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.shader = True
        print(f"Tree {self._name} now produce a shade of "
              f"{self._height}cm long and {self.trunk_diameter}cm wide.")
        self._tree_stats.increment_shade_calls()


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

    def age(self, age_rate: int = 1) -> None:
        super().age(age_rate)
        self.nutritional_value += 1

    def grow(self, growth_rate: float = 2.1) -> None:
        super().grow(growth_rate)
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 days_age: int, color:  str) -> None:
        super().__init__(name, height, days_age, color)
        self.count_seed = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.count_seed}")

    def bloom(self, number_of_seeds: int = 0) -> None:
        super().bloom()
        self.count_seed += number_of_seeds


def display_statistics(plant: Plant) -> None:
    plant.analytics.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_a_year(400)}	")
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
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)
    print("")

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_statistics(anonymous)
