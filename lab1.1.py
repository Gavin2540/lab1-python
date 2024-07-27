import math

def li_functions():
    levi = []
    n = int(input("Enter number of list elements: "))
    for i in range(n):
        ele = int(input(f"Enter element {i + 1}: "))
        levi.append(ele)
    
    print("List:", levi)
    
    # Sum of all elements
    Sum = sum(levi)
    print("Sum of all elements in the list:", Sum)
    
    # Product of all elements
    result = 1
    for x in levi:
        result *= x
    print("Product of all elements in the list:", result)
    
    # Largest element
    print("Largest element in the list:", max(levi))
    
    # Smallest element
    print("Smallest element in the list:", min(levi))

def print_matching_strings():
    strings = []
    n = int(input("How many strings do you want to input? "))
    for i in range(n):
        user_input = input(f"Enter string {i + 1}: ")
        strings.append(user_input)
    
    for index, string in enumerate(strings):
        if isinstance(string, str) and len(string) > 1:
            if string[0] == string[-1]:
                print(f"String: '{string}' at Index: {index}")

def pattern_1(n):
    for i in range(1, n + 1):
        for j in range(65, 65 + i):  # ASCII value of 'A' is 65
            print(chr(j), end='')
        print()  # For new line

def pattern_2(n):
    for i in range(1, n + 1):
        print("*" * i)

def list_to_dict(colors, codes):
    return [{"colorName": color, "colorCode": code} for color, code in zip(colors, codes)]

def even_No():
    for i in range(1, 50):
        if i % 2 == 0:
            print(i)

def sum_of_digits(number):
    number_str = str(number)
    total_sum = 0
    for digit in number_str:
        total_sum += int(digit)
    return total_sum

def reverse_number(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    reversed_number = int(reversed_str)
    return reversed_number

def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def total_area_and_contribution(triangle1, triangle2):
    area1 = area_of_triangle(*triangle1)
    area2 = area_of_triangle(*triangle2)
    total_area = area1 + area2
    contribution1 = (area1 / total_area) * 100
    contribution2 = (area2 / total_area) * 100
    return total_area, contribution1, contribution2

def print_person_info(people):
    for person in people:
        print(f"Name: {person['name']}")
        print(f"Age: {person['age']}")
        print(f"Blood Group: {person['blood_group']}")
        print("-" * 20)

def extract_rear_elements(tup, n):
    return tup[-n:]

def days_in_month(month, is_leap_year=False):
    months_days = {
        "January": 31, "February": 29 if is_leap_year else 28, "March": 31,
        "April": 30, "May": 31, "June": 30,
        "July": 31, "August": 31, "September": 30,
        "October": 31, "November": 30, "December": 31
    }
    return months_days.get(month, "Invalid month")

def main():
    while True:
        print("\nMenu")
        print("1. List Operations")
        print("2. Print Matching Strings")
        print("3. Pattern Printing 1")
        print("4. Pattern Printing 2")
        print("5. List to Dictionary")
        print("6. Even Numbers")
        print("7. Sum of Digits of a Four-Digit Number")
        print("8. Reverse a Four-Digit Number")
        print("9. Area of Triangles and Contribution")
        print("10. Print Person Info")
        print("11. Extract Rear Elements from Tuple")
        print("12. Days in Month Calculation")
        print("13. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            li_functions()
        elif choice == 2:
            print_matching_strings()
        elif choice == 3:
            n = int(input("Enter the number of rows: "))
            pattern_1(n)
        elif choice == 4:
            n = int(input("Enter the number of rows: "))
            pattern_2(n)
        elif choice == 5:
            colors = ["Black", "Red", "Maroon", "Yellow"]
            codes = ["000000", "FF0000", "800000", "FFFF00"]
            print(list_to_dict(colors, codes))
        elif choice == 6:
            even_No()
        elif choice == 7:
            number = int(input("Enter a four-digit number: "))
            print("Sum of digits:", sum_of_digits(number))
        elif choice == 8:
            number = int(input("Enter a four-digit number: "))
            print("Reversed number:", reverse_number(number))
        elif choice == 9:
            triangle1 = tuple(map(int, input("Enter the sides of the first triangle separated by spaces: ").split()))
            triangle2 = tuple(map(int, input("Enter the sides of the second triangle separated by spaces: ").split()))
            total_area, contribution1, contribution2 = total_area_and_contribution(triangle1, triangle2)
            print(f"Total area: {total_area}")
            print(f"Triangle 1 contribution: {contribution1}%")
            print(f"Triangle 2 contribution: {contribution2}%")
        elif choice == 10:
            people = [
                {"name": "Alice", "age": 25, "blood_group": "A+"},
                {"name": "Bob", "age": 30, "blood_group": "B+"},
                {"name": "Charlie", "age": 22, "blood_group": "O+"},
                {"name": "David", "age": 27, "blood_group": "AB+"},
                {"name": "Eve", "age": 35, "blood_group": "A-"},
                {"name": "Frank", "age": 28, "blood_group": "B-"},
                {"name": "Grace", "age": 32, "blood_group": "O-"},
                {"name": "Hank", "age": 29, "blood_group": "AB-"},
                {"name": "Ivy", "age": 24, "blood_group": "A+"},
                {"name": "Jack", "age": 26, "blood_group": "B+"}
            ]
            print_person_info(people)
        elif choice == 11:
            example_tuple = ('a', 'b', 'c', 'd', 'e')
            n = int(input("Enter the number of rear elements to extract: "))
            print("Rear elements:", extract_rear_elements(example_tuple, n))
        elif choice == 12:
            month = input("Enter the month: ")
            is_leap_year = input("Is it a leap year? (yes/no): ").lower() == 'yes'
            print(f"Days in {month}: {days_in_month(month, is_leap_year)}")
        elif choice == 13:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
