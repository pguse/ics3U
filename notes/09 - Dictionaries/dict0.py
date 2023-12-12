courses = { "Math" : 75, "English" : 90, "History" : 85, "French" : 70, "Geography" : 80, "Science" : 95}

for k,v in courses.items():
    print( f"{k:<10} {v:>3}".format(k,v) )