from typing import Optional, Union, Tuple


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

        height = _parse_height_input(height_input)
        if height is not None and height > 0:
            return height
        print("Invalid input. Please enter a positive, non-zero value for height.")

def _parse_height_input(height_input: str) -> Optional[float]:
    try:
        if '.' in height_input or ',' in height_input:
            return float(height_input.replace('cm', '').replace(',', '.'))
        return float(height_input) / 100
    except ValueError:
        return None