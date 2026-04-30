# nested dictionary
desi_menu = {
    "Starter":{
        "Soup": 50,
        "Wontongs": 200,
        "Chicken Tender": 300,
        "Drum Sticks": 450,
        "Masala Chips": 100,
    },
    "Sauces":{
        "Mint Chutney": 20,
        "Tamarind Sauce": 25,
        "Raita": 30,
        "Ketchup": 50,
    },
    "Main Course":{
        "Chicken Biryani": 400,
        "Beef Biryani": 600,
        "Beef Nehari": 500,
        "Chicken Makhni Handi": 600,
        "Chicken Karahi": 500,
        "Chicken White Karahi": 600,
        "Mutton Karahi" : 1200,
        "Mutton White Karahi" : 1200,
        "Beef Qorma" : 650,
    },
    "Dessert": {
        "Ras Malai": 200,
        "Kunafa": 200,
        "Three Mill Cake": 300,
        "Choco Lava": 250,
        "Ice Cream": 110,
    },
    "Naan/Pratha": {
        "Normal Naan": 30,
        "Garlic Naan": 50,
        "Chappati": 20,
        "Special Naan": 90,
    },
    "Drinks": {
        "Cold Drinks Regular": 90,
        "Oreo Milk Shake": 110,
        "Slush": 110,
        "Lassi": 90,
        "Chai": 90
    }
}


# Taking User Input
student_name = input("Enter Student Name: ")
roll_no = input("Enter Student Roll No: ")
marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for Subject 'Max: 100' {i}: "))
    if m > 100:
        print("Invalid marks entered. Storing 100 as marks for this subject.")
        m = 100
    elif m < 0:
        print("Invalid marks entered. Storing 0 as marks for this subject.")
        m = 0
    marks.append(m)

student_data = {
    "name": student_name,
    "roll_no": roll_no,
    "marks": marks
}

total_marks = sum(student_data["marks"])
percentage = (total_marks / 500) * 100

print("\n" + "="*50)
print(f"Student Name: {student_data['name']}")
print(f"Roll Number: {student_data['roll_no']}")
print(f"Total Marks: {total_marks}")
for i, mark in enumerate(student_data["marks"]):
    print(f"Marks for Subject {i+1}: {mark}")
print(f"Total Percentage: {round(percentage,2)}%")
print("\n" + "="*50)