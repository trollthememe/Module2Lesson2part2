#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

#Buggy Code:

#attendees = input("Enter number of attendees: ")
#venue = "large hall" if attendees > 100 else "conference room"
#print(venue)

#######------ Buggy code above while corrected code is below and attached to task 3

# Task 2: Venue Selection
#Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

#Task 3: Catering Choices
#Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
equipment = "audio system" if attendees > 100 else "projector"
print("Based on the information provided your event could use a(n):", equipment)
food = input("Do you prefer veg or non-veg?")
food = "Veggie Delight Caterers" if food == "veg" else "Gourmet Meals Caterers"
print(food)

