from typing import Optional, Union, Tuple

class BMICalculator:
    def calculate_bmi(self, weight: float, height: float) -> float:
        return weight / (height * height)

    def classify_bmi(self, bmi: float) -> str:
        bmi_categories = [
            ((0, 16.0), 'Starvation'),
            ((16.0, 16.99), "You are too skinny"),
            ((17.0, 24.99), "Your weight is okay!"),
            ((25.0, 29.99), "You are overweight!"),
            ((30.0, 34.99), "You are stage 1 obesity"),
            ((35.0, 39.99), "You are stage 2 obesity"),
            ((40.0, float('inf')), "Extreme obesity")
        ]

        for (range_start, range_end), category in bmi_categories:
            if range_start <= bmi <= range_end:
                return category
        return "BMI out of range"

def get_weight() -> Optional[float]:
    while True:
        weight_input = input("Enter your weight (kg) or 'q' to quit: ")
        if weight_input.lower() == 'q':
            return None

        try:
            weight = float(weight_input)
            if weight <= 0:
                print("Weight must be a positive, non-zero value.")
                continue
            return weight

        except ValueError:
            print("Invalid input. Please enter a numeric value for weight.")

def get_height() -> Optional[float]:
    while True:
        height_input = input("Enter your height in meters or centimeters, or 'q' to quit: ").strip().lower()

        if height_input == 'q':
            return None

        height = parse_height_input(height_input)
        if height is not None and height > 0:
            return height
        print("Invalid input. Please enter a positive, non-zero value for height.")

def parse_height_input(height_input: str) -> Optional[float]:
    try:
        if '.' in height_input or ',' in height_input:
            return float(height_input.replace('cm', '').replace(',', '.'))
        return float(height_input) / 100
    except ValueError:
        return None
