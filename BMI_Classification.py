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

