# Dictionaries for course information
rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Ask the user for a course number
course = input("Enter a course number (e.g., CSC101): ")

# Look up and display the course information
if course in rooms:
    print(f"Course: {course}")
    print(f"Room Number: {rooms[course]}")
    print(f"Instructor: {instructors[course]}")
    print(f"Meeting Time: {meeting_times[course]}")
else:
    print("Sorry, that course number was not found.")
