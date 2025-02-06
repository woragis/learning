from typing import List


class Food:
    base_hearts = 1

    def __init__(self, igredients: List[str]) -> None:
        self.igredientes = igredients
        self.hearts = Food.calculate_hearts(igredients)
        pass

    @classmethod
    def calculate_hearts(cls, igredients: List[str]) -> int:
        hearts = cls.base_hearts
        for igredient in igredients:
            if 'hearty' in igredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts: int):
        food = cls(igredients=[])
        food.hearts = hearts
        return food


def main():
    mushroom_skewer = Food(igredients=['Mushroom', 'Hearty Mushroom'])
    print(f'This skewer heals: {mushroom_skewer.hearts} hearts!')

    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f'This skewer heals: {mushroom_skewer.hearts} hearts!')


if __name__ == '__main__':
    main()
