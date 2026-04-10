class food_item:
    """A food item with its core nutritional values."""

    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = float(calories)
        self.protein = float(protein)
        self.carbohydrates = float(carbohydrates)
        self.fat = float(fat)


def report_daily_nutrition(consumed_items):
    """Input: consumed_items, a list of food_item objects consumed in 24 hours.
    Nutritional values are treated as per-serving values.

    Returns:
        dict: Total calories, protein, carbohydrates, fat, and any warnings.
    """
    total_calories = 0.0
    total_protein = 0.0
    total_carbohydrates = 0.0
    total_fat = 0.0

    for item in consumed_items:
        if not isinstance(item, food_item):
            raise TypeError("Each consumed item must be an instance of food_item.")
        total_calories += item.calories
        total_protein += item.protein
        total_carbohydrates += item.carbohydrates
        total_fat += item.fat

    warnings = []
    if total_calories > 2500:
        warnings.append("WARNING: Daily calories exceed 2500 kcal.")
    if total_fat > 90:
        warnings.append("WARNING: Daily fat exceeds 90 g.")

    print("24-hour nutrition summary")
    print(f"Total calories: {total_calories:.1f} kcal")
    print(f"Total protein: {total_protein:.1f} g")
    print(f"Total carbohydrates: {total_carbohydrates:.1f} g")
    print(f"Total fat: {total_fat:.1f} g")
    if warnings:
        for message in warnings:
            print(message)
    else:
        print("No calorie or fat warning.")

    return {
        "total_calories": total_calories,
        "total_protein": total_protein,
        "total_carbohydrates": total_carbohydrates,
        "total_fat": total_fat,
        "warnings": warnings,
    }


if __name__ == "__main__":
    # Example class instances and function call
    apple = food_item("Apple", 95, 0, 25, 0)
    banana = food_item("Banana", 105, 1, 27, 0)
    orange = food_item("Orange", 62, 1, 15, 0)
    broccoli = food_item("Broccoli", 31, 3, 6, 0)
    blueberries = food_item("Blueberries", 84, 1, 22, 1)
    mango = food_item("Mango", 99, 1, 25, 1)

    day_food = [
        apple,
        banana,
        orange,
        broccoli,
        blueberries,
        mango,
    ]
    report_daily_nutrition(day_food)
