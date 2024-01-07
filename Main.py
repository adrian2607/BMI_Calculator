from datetime import datetime


def calculate_bmi(weight, height):
    return weight / (height * height)

def classify_bmi(bmi):
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

def time_and_date(current_time=datetime.now()):
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

def save_to_file(data):
    with open("bmi_results.txt", "a") as file:
        file.write(data + "\n")

def main():
    try:
        weight = float(input("Enter your weight (kg): "))
        height = input("Enter your height (m or cm): ")


    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    bmi = calculate_bmi(weight, height)
    classification = classify_bmi(bmi)

    result_message = f"{time_and_date()}: Your BMI is: {bmi:.2f} {classification}"
    print(result_message)

    # Save result to file
    save_to_file(result_message)

if __name__ == "__main__":
    main()
