class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days_age = days_age

    def show(self) -> None:
        print(f"{self.name} : {self.height}cm, {self.days_age} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
