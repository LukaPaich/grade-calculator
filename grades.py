import json
import sys

weight_table = {
    "A": 4,
    "B": 3.38,
    "C": 2.77,
    "D": 2.16,
    "E": 1.55,
    "F": 0,
    "S": 4,
}

def print_gpa(grades_str: str):
    grades = json.loads(grades_str)
    total_score = 0
    total_credits = 0
    for semester in grades:
        for course in semester["source"]["data"]:
            credit = course["credit"]
            grade = course["result"]

            if grade is None or credit is None:
                continue

            total_score += credit * weight_table[grade]
            total_credits += credit
    
    print("Total Credits:", total_credits)
    print("Weighted GPA: ", total_score / total_credits)


def main():
    args = sys.argv
    if len(args) < 2:
        print("USAGE: grades.py [grades.json]")
        return

    with open(args[1], 'r', encoding='utf-8') as f:
        print_gpa(f.read())

if __name__ == "__main__":
    main()