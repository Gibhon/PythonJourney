# nums = [1, 2, 3, 4]
# print(max(nums))


# exit()

students = {
    1: {"name": "Gibhon", "class": 11, "percentage": 88.5},
    2: {"name": "Suyou", "class": 12, "percentage": 91.2},
    3: {"name": "Aria", "class": 10, "percentage": 76.0}
}

searched_name = input("Enter the student's name:").capitalize()
names = [value["name"] for value in students.values()]
if searched_name not in names:
    print("student Doesnt Exist in the records.")
else:
    for value in students.values():
        if value["name"] == searched_name:
            print(f"percetage: {value["percentage"]}")



