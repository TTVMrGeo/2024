import json, os

stop = False

while not stop:

    def read_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
        
    def write_json(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            
    choice = input("What do you want to do?\n1. Accept\n2. Display\n3. Search\n4. Delete\n5. Update\n6. Exit\n> ")

    def accept():
        os.system("cls")
        name = input("Enter the name of the student: ")
        surname = input("Enter the surname of the student: ")
        age = int(input("Enter the age of the student: "))
        gender = input("Enter the gender of the student: ")
        grade = int(input("Enter the grade of the student: "))
        
        base_data = {"name": name, "surname": surname, "age": age, "gender": gender, "grade": grade}
        data = read_json("database.json")
        next_index = len(data)+1
        data[next_index] = base_data
        write_json("database.json", data)

    def display():
        data = read_json("database.json")
        os.system("cls")
        for key, value in data.items():
            print(f"Student {key}:")
            print(f"Name: {value['name']}")
            print(f"Surname: {value['surname']}")
            print(f"Age: {value['age']}")
            print(f"Gender: {value['gender']}")
            print(f"Grade: {value['grade']}\n")

    def serach():
        pass

    def delete():
        data = read_json("database.json")
        os.system("cls")
        data.pop(int(input("Enter the index of the student you want to delete: ")))

    def update():
        pass
    
    match choice:
        case "1":
            accept()
        case "2":
            display()
        case "3":
            pass
        case "4":
            delete()
        case "5":
            pass
        case "6":
            stop = True   
        case _:
            print("That's not a valid choice.")
        