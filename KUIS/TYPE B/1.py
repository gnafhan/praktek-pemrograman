hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins += dura

while mins > 60:
    mins -= 60
    hour += 1

if mins < 10:
    print(str(hour)+":"+"0"+str(mins))
else:
    print(str(hour)+":"+str(mins))
