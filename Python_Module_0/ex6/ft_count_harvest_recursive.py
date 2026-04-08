def ft_count_harvest_recursive() -> None:
    def recursive_count(days: int) -> None:
        if days == 0:
            return
        recursive_count(days - 1)
        print(f"Day {days}")
    days = int(input("Days until harvest: "))
    recursive_count(days)
    print("Harvest time!")
