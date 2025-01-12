def calculate_grade():
    try:
        subject1 = float(input("Subject 1 marks: "))
        subject2 = float(input("Subject 2 marks: "))
        subject3 = float(input("Subject 3 marks: "))
        average = (subject1 + subject2 + subject3) / 3
        if average >= 90:
            grade = "A"
        elif 80 <= average < 90:
            grade = "B"
        elif 70 <= average < 80:
            grade = "C"
        else:
            grade = "Fail"
        print(f"Average Marks: {average:.2f}")
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")
calculate_grade()
