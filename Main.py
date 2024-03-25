from datetime import *
from DataStorage import *
from bmi_calculator import *
from raw_data import *


def main():
    raw_data = RawData()
    bmi_calculator = BMICalculator()
    data_storage = DataStorage()

    while True:
        weight = raw_data.get_weight()
        if weight is None:
            break

        height = raw_data.get_height()
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
