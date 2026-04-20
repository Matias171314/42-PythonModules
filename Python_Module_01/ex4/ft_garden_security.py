class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._days_age = 0
        self.set_height(height)
        self.set_age(days_age)

    def show(self) -> None:
        print(f"{self.name} : {self._height}cm, {self._days_age} days old")

    def grow(self, growth_rate: float = 0.8) -> None:
        self._height = round(self._height + growth_rate, 1)

    def age(self) -> None:
        self._days_age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days_age = new_age


if __name__ == "__main__":
    rose = Plant("rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    print("")
    rose.set_height(25.0)
    print(f"Height updated: {rose.get_height()}")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()}")
    print("")
    rose.set_height(-1.8)
    rose.set_age(-7)
    print("")
    print("Current state: ", end="")
    rose.show()
