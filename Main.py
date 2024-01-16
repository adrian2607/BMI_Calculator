from datetime import datetime

from Calculator_BMI import *

from BMI_Classification import classify_bmi
from Save_DB import *


def time_and_date(current_time=datetime.now()):
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

def save_to_file(data):
    with open("bmi_results.txt", "a") as file:
        file.write(data + "\n")

def main():
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))


    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)

    result_message = f"{time_and_date()}: Your BMI is: {bmi:.2f} {classification}"
    print(result_message)

    # Save result to file
    save_to_file(result_message)
    db_saver = Save_DB()
    db_saver.save_to_database(weight, height, bmi, classification)
if __name__ == "__main__":
    main()
