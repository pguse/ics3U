courses = { "Math" : 75, "English" : 90, "History" : 85, "French" : 70, "Geography" : 80, "Science" : 95, "Spanish": 75}

# Check for a key not found in the dictionary
if "Phys. Ed." in courses:
    print( "Phys.Ed")
else:
    print( "Course not found.")
    
# Check for a key found in the dictionary
if "Spanish" in courses:
    print( courses["Spanish"] )
else:
    print("Course not found.")