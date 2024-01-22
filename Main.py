from datetime import datetime
from BMI_Classification import classify_bmi
from Calculator_BMI import calculate_bmi
from DataStorage import *


def get_time_and_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_to_file(data):
    with open("bmi_results.txt", "a") as file:
        file.write(data + "\n")


def get_height():
    while True:
        height_input = input("Enter your height in meters or centimeters, or 'q' to quit: ")
        if height_input.lower() == 'q':
            return None

        try:
            if '.' in height_input or ',' in height_input:
                height = float(height_input.replace('cm', '').replace(',', '.'))
            else:
                height = float(height_input) / 100

            return height

        except ValueError:
            print("Invalid input. Please enter a numeric value for height.")


def main():
    while True:
        try:
            weight_input = input("Enter your weight (kg) or 'q' to quit: ")
            if weight_input.lower() == 'q':
                break

            weight = float(weight_input)

            height = get_height()
            if height is None:
                break

            if weight == 0 or height == 0:
                print("Weight and height must be non-zero values.")
                return

            bmi = calculate_bmi(weight, height)
            classification = classify_bmi(bmi)

            current_time = get_time_and_date()
            result_message = f"{current_time}: Your BMI is: {bmi:.2f} {classification}"
            print(result_message)

            save_to_file(result_message)
            db_saver = DataStorage()
            db_saver.save_to_database(weight, height, bmi, classification, current_time)

        except ValueError as e:
            print(f"Error: {e}")
            print("Invalid input. Please enter numeric values.")
            return
        except Exception as e:
            print(f"Error: {e}")
            return


if __name__ == "__main__":
    main()
