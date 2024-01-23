from datetime import datetime
from DataStorage import *


class BMICalculator:
    def calculate_bmi(self, weight, height):
        return weight / (height * height)

    def classify_bmi(self, bmi):
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


def get_time_and_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_weight():
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


def get_height():
    while True:
        height_input = input("Enter your height in meters or centimeters, or 'q' to quit: ").strip().lower()

        if height_input == 'q':
            return None

        height = parse_height_input(height_input)
        if height is not None and height > 0:
            return height
        print("Invalid input. Please enter a positive, non-zero value for height.")


def parse_height_input(height_input):
    try:
        if '.' in height_input or ',' in height_input:
            return float(height_input.replace('cm', '').replace(',', '.'))
        return float(height_input) / 100
    except ValueError:
        return None


def main():
    bmi_calculator = BMICalculator()
    data_storage = DataStorage()

    while True:
        weight = get_weight()
        if weight is None:
            break

        height = get_height()
        if height is None:
            break

        bmi = bmi_calculator.calculate_bmi(weight, height)
        classification = bmi_calculator.classify_bmi(bmi)

        current_time = get_time_and_date()
        result_message = f"{current_time}: Your BMI is: {bmi:.2f} {classification}"
        print(result_message)

        data_storage.save_to_file(result_message)
        data_storage.save_to_database(weight, height, bmi, classification, current_time)


if __name__ == "__main__":
    main()
