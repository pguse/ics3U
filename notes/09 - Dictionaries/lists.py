courses = ["Math", "English", "History", "French", "Geography", "Science"]
marks = [75, 90, 85, 70, 80, 95]

for i in range( len(courses) ):
    print( f"{courses[i]:<10} {marks[i]:>3}")