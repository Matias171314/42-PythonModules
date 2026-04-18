class Plant:
    def __init__(self, name: str, height: float, days_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days_age = days_age

    def show(self) -> None:
        print(f"{self.name} : {self.height}cm, {self.days_age} days old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.days_age += 1


if __name__ == "__main__":
    rose = Plant("rose", 25.0, 30)
    oak = Plant("oak", 200.0, 365)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("fern", 15.0, 120)
    garden_plants = [rose, oak, cactus, sunflower, fern]

    print("=== Plant Factory Output ===")
    for plant in garden_plants:
        print("Created: ", end="")
        plant.show()
