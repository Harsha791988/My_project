import csv

def read_student_file(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            students = list(reader)

        if not students:
            raise ValueError("Student file is empty.")

        marks = []
        print("\n--- Student Records ---")
        for record in students:
            if len(record) < 3:
                print("Invalid record:", record)
                continue
            roll, name, score = record
            try:
                score = float(score)
                marks.append(score)
                print(f"Roll: {roll}, Name: {name}, Marks: {score}")
            except ValueError:
                print("Invalid marks:", record)

        if marks:
            print("\n--- Academic Summary ---")
            print(f"Total Students: {len(marks)}")
            print(f"Average Marks: {sum(marks)/len(marks):.2f}")
            print(f"Highest Marks: {max(marks)}")
            print(f"Lowest Marks: {min(marks)}")

    except Exception as e:
        print("Error:", e)

# Example usage
read_student_file("students.csv")
