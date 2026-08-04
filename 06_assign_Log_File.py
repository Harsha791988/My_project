import os

def process_log_file(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError("Log file not found.")

        with open(filename, "r") as f:
            lines = f.readlines()

        if not lines:
            raise ValueError("Log file is empty.")

        counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for line in lines:
            if "INFO" in line:
                counts["INFO"] += 1
            elif "WARNING" in line:
                counts["WARNING"] += 1
            elif "ERROR" in line:
                counts["ERROR"] += 1

        print("\n--- Log Summary ---")
        print(f"Total Records: {len(lines)}")
        for level, count in counts.items():
            print(f"{level}: {count}")

        if counts["ERROR"] > 0:
            print("⚠ Critical issues detected!")

    except Exception as e:
        print("Error:", e)

# Example usage
process_log_file("system1.log")
