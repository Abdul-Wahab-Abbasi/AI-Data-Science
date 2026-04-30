# Creating and Accessing Dictionary
# bioData = {
#     "name": "Abdul Wahab",
#     "age": 21,
#     "city": "Hyderabad",
#     "hobbies": ["reading", "traveling", "coding"],
#     "isEmployed": True,
#     "skills": {
#         "programming": ["Python", "PHP", "JavaScript", "C++"],
#         "languages": ["English", "Spanish"],
#         "softSkills": ["communication", "problem-solving", "teamwork"]
#     }
# }

# print("=== Bio Data ===")
# print(f"Name: {bioData['name']}")
# print(f"Age: {bioData['age']}")
# print(f"City: {bioData['city']}")
# print("Hobbies:")
# for hobby in bioData["hobbies"]:
#     print(f" - {hobby}")
# print(f"Employed: {'Yes' if bioData['isEmployed'] else 'No'}")
# print("Skills:")
# print(" Programming:")
# for skill in bioData["skills"]["programming"]:
#     print(f"  - {skill}")
# print(" Languages:")
# for language in bioData["skills"]["languages"]:
#     print(f"  - {language}")
# print(" Soft Skills:")
# for softSkill in bioData["skills"]["softSkills"]:
#     print(f"  - {softSkill}")

# # using dictionary method
# car = dict(model = "Alto", brand = "Suzuki", year = 2002)

# print(car)

# # Change the "year" to 2018:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018

# # Update the "year" of the car by using the update() method:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# # Add a color item to the dictionary by using the update() method:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)

# # The pop() method removes the item with the specified key name:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)


# # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)


# # The del keyword removes the item with the specified key name:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)


# # The clear() method removes all items from the dictionary resulting empty dictionary {}.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)
